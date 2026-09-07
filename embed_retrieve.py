"""Embed ingested chunks in ChromaDB and retrieve relevant source context."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import chromadb
from sentence_transformers import SentenceTransformer




MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "howard-study-spots"
DEFAULT_DB_DIR = Path("chroma_db")
DEFAULT_TOP_K = 5


@dataclass(frozen=True)
class RetrievedChunk:
    text: str
    source_id: int
    title: str
    url: str
    chunk_id: int
    distance: float


def load_chunks(chunks_path: Path) -> list[dict[str, Any]]:
    """Load and validate chunk records produced by ingest.py."""
    chunks: list[dict[str, Any]] = []
    required_fields = {"source_id", "title", "url", "chunk_id", "text"}

    with chunks_path.open("r", encoding="utf-8") as chunks_file:
        for line_number, line in enumerate(chunks_file, start=1):
            if not line.strip():
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON in {chunks_path} on line {line_number}"
                ) from error

            if not isinstance(record, dict):
                raise ValueError(
                    f"Expected an object in {chunks_path} on line {line_number}"
                )

            missing_fields = required_fields - record.keys()
            if missing_fields:
                raise ValueError(
                    f"{chunks_path}:{line_number} is missing "
                    f"{sorted(missing_fields)}"
                )

            if not isinstance(record["text"], str) or not record["text"].strip():
                raise ValueError(
                    f"{chunks_path}:{line_number} has empty chunk text"
                )

            chunks.append(record)

    if not chunks:
        raise ValueError(f"No chunks found in {chunks_path}")

    return chunks


def get_collection(
    db_dir: Path = DEFAULT_DB_DIR,
    reset: bool = False,
):
    """Open the persistent ChromaDB collection used by this project."""
    client = chromadb.PersistentClient(path=str(db_dir))

    if reset:
        try:
            client.delete_collection(COLLECTION_NAME)
        except (ValueError, chromadb.errors.NotFoundError):
            pass

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"description": "Howard University and DC study locations"},
    )


def create_index(
    chunks_path: Path,
    db_dir: Path = DEFAULT_DB_DIR,
    reset: bool = False,
) -> int:
    """Embed chunks and store their documents and source metadata."""
    chunks = load_chunks(chunks_path)
    model = SentenceTransformer(MODEL_NAME)
    collection = get_collection(db_dir, reset=reset)

    texts = [chunk["text"] for chunk in chunks]
    ids = [
        f"source-{chunk['source_id']}-chunk-{chunk['chunk_id']}"
        for chunk in chunks
    ]
    metadatas = [
        {
            "source_id": int(chunk["source_id"]),
            "title": str(chunk["title"]),
            "url": str(chunk["url"]),
            "chunk_id": int(chunk["chunk_id"]),
        }
        for chunk in chunks
    ]
    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True,
    ).tolist()

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
    )
    return len(chunks)


def retrieve(
    query: str,
    db_dir: Path = DEFAULT_DB_DIR,
    top_k: int = DEFAULT_TOP_K,
) -> list[RetrievedChunk]:
    """Return the top-k chunks ranked by semantic similarity."""
    if not query.strip():
        raise ValueError("Query cannot be empty")
    if top_k < 1:
        raise ValueError("top_k must be at least 1")

    client = chromadb.PersistentClient(path=str(db_dir))
    collection = client.get_collection(name=COLLECTION_NAME)
    count = collection.count()
    if count == 0:
        raise RuntimeError("The ChromaDB collection is empty")

    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode(
        [query],
        normalize_embeddings=True,
    ).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=min(top_k, count),
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]
    return [
        RetrievedChunk(
            text=document,
            source_id=int(metadata["source_id"]),
            title=str(metadata["title"]),
            url=str(metadata["url"]),
            chunk_id=int(metadata["chunk_id"]),
            distance=float(distance),
        )
        for document, metadata, distance in zip(documents, metadatas, distances)
    ]


def format_context(chunks: list[RetrievedChunk]) -> str:
    """Format retrieved chunks for the generation stage with citations."""
    return "\n\n".join(
        f"[Context {index}]\n"
        f"Source: {chunk.title}\n"
        f"URL: {chunk.url}\n"
        f"Source ID: {chunk.source_id}\n"
        f"Chunk ID: {chunk.chunk_id}\n"
        f"Content:\n{chunk.text}"
        for index, chunk in enumerate(chunks, start=1)
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    index_parser = subparsers.add_parser("index", help="Build the ChromaDB index")
    index_parser.add_argument(
        "--chunks",
        type=Path,
        default=Path("documents/chunks.jsonl"),
    )
    index_parser.add_argument("--db-dir", type=Path, default=DEFAULT_DB_DIR)
    index_parser.add_argument(
        "--reset",
        action="store_true",
        help="Delete the existing collection before indexing",
    )

    retrieve_parser = subparsers.add_parser(
        "retrieve",
        help="Retrieve context for a question",
    )
    retrieve_parser.add_argument("query")
    retrieve_parser.add_argument("--db-dir", type=Path, default=DEFAULT_DB_DIR)
    retrieve_parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)

    args = parser.parse_args()
    if args.command == "index":
        count = create_index(args.chunks, args.db_dir, reset=args.reset)
        print(f"Indexed {count} chunks in {args.db_dir}")
        return

    print(format_context(retrieve(args.query, args.db_dir, args.top_k)))


if __name__ == "__main__":
    main()

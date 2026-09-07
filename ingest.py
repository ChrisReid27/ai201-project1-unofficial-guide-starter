"""Fetch the project sources, clean them to raw text, and create RAG chunks."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse
from urllib.request import Request, urlopen


CHUNK_SIZE = 1000 # Target chunk size in characters, between 1000 and 1200.
OVERLAP = 200 # Chunk overlap in characters, between 150 and 200.
USER_AGENT = "python:ai201-unofficial-guide-ingestion:v1.0 (educational project)"


@dataclass(frozen=True)
class Source:
    source_id: int
    title: str
    url: str


SOURCES = (
    Source(1, "Best Places To Study On Campus", "https://thehilltoponline.com/2023/08/21/best-places-to-study-on-campus/"),
    Source(2, "Seven Places to Study on Howard's Campus", "https://thedig.howard.edu/all-stories/seven-places-study-howards-campus"),
    Source(3, "Howard Founders Library", "https://founders.howard.edu/"),
    Source(4, "Howard Business Library", "https://businesslibrary.howard.edu/"),
    Source(5, "Howard University quiet meeting places", "https://www.reddit.com/r/HowardUniversity/comments/1qjt4e2/where_is_a_quiet_place_on_campus_that_i_can_take/"),
    Source(6, "Louis Stokes Health Science Library About Page", "https://hsl.howard.edu/library/about"),
    Source(7, "Study and Remote Work Locations in DC", "https://docs.google.com/spreadsheets/d/1SzIld1R8k2QeIKut5YacZTwVTanlP2O3ZxWdvn-XFv0/edit?gid=1240342982#gid=1240342982"),
    Source(8, "Most beautiful places to study or read in DC", "https://www.reddit.com/r/washingtondc/comments/8rh2bj/most_beautiful_places_to_studyread_in_dc/"),
    Source(9, "Underrated study spots in DC", "https://www.reddit.com/r/washingtondc/comments/1kggh4w/underrated_study_spots/"),
    Source(10, "Best cafes in DC for working or studying", "https://www.reddit.com/r/washingtondc/comments/1521vi4/best_cafes_in_dc_for_working_or_studying/"),
)


class TextExtractor(HTMLParser):
    """Extract visible HTML text while preserving useful block boundaries."""

    BLOCK_TAGS = {"article", "br", "div", "h1", "h2", "h3", "h4", "li", "p", "section", "tr"}
    IGNORED_TAGS = {"canvas", "footer", "head", "nav", "noscript", "script", "style", "svg"}

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self.IGNORED_TAGS:
            self.ignored_depth += 1
        elif not self.ignored_depth and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.IGNORED_TAGS and self.ignored_depth:
            self.ignored_depth -= 1
        elif not self.ignored_depth and tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.ignored_depth:
            self.parts.append(data)


def clean_text(raw: str, content_type: str = "") -> str:
    """Convert HTML or CSV into normalized, searchable plain text."""
    if "html" in content_type.lower() or re.search(r"<(?:html|body|p|div|article)\b", raw, re.I):
        parser = TextExtractor()
        parser.feed(raw)
        raw = "".join(parser.parts)
    lines = (re.sub(r"[ \t]+", " ", line).strip() for line in raw.splitlines())
    return "\n".join(line for line in lines if line)


def sheet_csv_url(url: str) -> str:
    parsed = urlparse(url)
    match = re.search(r"/spreadsheets/d/([^/]+)", parsed.path)
    if not match:
        return url
    query = parse_qs(parsed.query)
    gid = query.get("gid", ["0"])[0]
    return f"https://docs.google.com/spreadsheets/d/{match.group(1)}/export?{urlencode({'format': 'csv', 'gid': gid})}"


def reddit_json_url(url: str) -> str:
    """Convert a Reddit thread URL to its JSON endpoint."""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    if not path.endswith(".json"):
        path += ".json"
    return urlunparse((parsed.scheme, parsed.netloc, path, "", parsed.query, ""))


def extract_reddit_text(payload: object) -> str:
    """Recursively collect Reddit post titles, bodies, and comment bodies."""
    parts: list[str] = []

    def visit(value: object) -> None:
        if isinstance(value, list):
            for item in value:
                visit(item)
            return
        if not isinstance(value, dict):
            return

        kind = value.get("kind")
        data = value.get("data")
        if kind in {"t3", "t1"} and isinstance(data, dict):
            if kind == "t3":
                title = data.get("title")
                body = data.get("selftext")
                if isinstance(title, str) and title.strip():
                    parts.append(title)
                if isinstance(body, str) and body.strip():
                    parts.append(body)
            else:
                body = data.get("body")
                if isinstance(body, str) and body.strip():
                    parts.append(body)
            visit(data.get("replies"))
            return

        for child in value.values():
            visit(child)

    visit(payload)
    return clean_text("\n".join(parts))


def fetch_source(source: Source) -> str:
    is_reddit = "reddit.com/" in source.url
    if is_reddit:
        url = reddit_json_url(source.url)
    elif "docs.google.com/spreadsheets" in source.url:
        url = sheet_csv_url(source.url)
    else:
        url = source.url
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json" if is_reddit else "*/*"})
    with urlopen(request, timeout=30) as response:
        body = response.read().decode(response.headers.get_content_charset() or "utf-8", errors="replace")
        content_type = response.headers.get_content_type()
    if is_reddit:
        return extract_reddit_text(json.loads(body))
    if content_type == "text/csv":
        rows = csv.reader(io.StringIO(body))
        body = "\n".join(" | ".join(cell.strip() for cell in row) for row in rows)
    return clean_text(body, content_type)


def load_source_text(source: Source, raw_dir: Path) -> str:
    """Load a manually curated source without changing its text."""
    path = raw_dir / f"{source.source_id:02d}.txt"
    if not path.exists():
        raise FileNotFoundError(f"Missing source file: {path}")
    return path.read_text(encoding="utf-8").strip()


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> list[str]:
    """Create word-boundary chunks of roughly 1,100 characters with overlap."""
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        if end < len(text):
            boundary = text.rfind(" ", start + chunk_size // 2, end)
            if boundary > start:
                end = boundary
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        next_start = max(start + 1, end - overlap)
        while next_start < len(text) and not text[next_start].isspace():
            next_start += 1
        while next_start < len(text) and text[next_start].isspace():
            next_start += 1
        start = next_start
    return chunks


def run(output_dir: Path, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> int:
    raw_dir = output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    chunks_path = output_dir / "chunks.jsonl"
    count = 0
    with chunks_path.open("w", encoding="utf-8") as chunks_file:
        for source in SOURCES:
            print(f"Loading {source.source_id}: {source.title}")
            text = load_source_text(source, raw_dir)
            for index, chunk in enumerate(chunk_text(text, chunk_size, overlap)):
                record = {"source_id": source.source_id, "title": source.title, "url": source.url, "chunk_id": index, "text": chunk}
                chunks_file.write(json.dumps(record, ensure_ascii=True) + "\n")
                count += 1
    print(f"Wrote {count} chunks to {chunks_path}")
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("documents"), help="Output directory (default: documents)")
    parser.add_argument("--chunk-size", type=int, default=CHUNK_SIZE, help="Target chunk size in characters (default: 1100)")
    parser.add_argument("--overlap", type=int, default=OVERLAP, help="Chunk overlap in characters (default: 175)")
    args = parser.parse_args()
    run(args.output, args.chunk_size, args.overlap)


if __name__ == "__main__":
    main()
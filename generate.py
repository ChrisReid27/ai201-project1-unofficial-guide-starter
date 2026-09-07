"""Generate grounded answers from retrieved Howard study-spot context."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv
from groq import Groq

from embed_retrieve import RetrievedChunk, format_context, retrieve


MODEL_NAME = "openai/gpt-oss-120b"
FALLBACK_ANSWER = "Sorry, I don't have enough information on that."

SYSTEM_PROMPT = f"""You answer questions about Howard University and Washington, DC study locations.
Use only the information in the retrieved documents supplied by the user. Do not use
your general knowledge, assumptions, or information from the URLs themselves.
If the documents do not contain enough information to answer, say exactly:
\"{FALLBACK_ANSWER}\"

Return only this answer section; the application will append the source list:
Answer:
<a concise answer grounded in the documents, with inline citations such as [1]>

Only cite sources that support the answer. Use the context number shown in the
documents for each citation. Never invent a source, URL, operating hour, or detail.
"""


@dataclass(frozen=True)
class GeneratedAnswer:
    answer: str
    sources: list[RetrievedChunk]


def build_messages(question: str, chunks: list[RetrievedChunk]) -> list[dict[str, str]]:
    """Build the grounded chat request sent to Groq."""
    if not question.strip():
        raise ValueError("Question cannot be empty")
    if not chunks:
        raise ValueError("At least one retrieved chunk is required")

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                "Retrieved documents:\n\n"
                f"{format_context(chunks)}\n\n"
                f"Question: {question.strip()}"
            ),
        },
    ]


def _source_list(chunks: list[RetrievedChunk]) -> str:
    """Append a deterministic source list so attribution survives model formatting."""
    source_contexts: dict[tuple[str, str], list[int]] = {}
    for context_number, chunk in enumerate(chunks, start=1):
        source_contexts.setdefault((chunk.title, chunk.url), []).append(context_number)

    lines = ["\n\nSources:"]
    lines.extend(
        f"- [{', '.join(map(str, context_numbers))}] {title} — {url}"
        for (title, url), context_numbers in source_contexts.items()
    )
    return "\n".join(lines)


def generate_answer(
    question: str,
    chunks: list[RetrievedChunk],
    client: Groq | None = None,
) -> GeneratedAnswer:
    """Generate an answer using only the supplied retrieved chunks."""
    load_dotenv()
    if client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key or api_key == "your_key_here":
            raise RuntimeError("Set GROQ_API_KEY in .env before starting the app")
        client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=build_messages(question, chunks),
        temperature=0,
    )
    answer = response.choices[0].message.content.strip()
    if not answer:
        answer = FALLBACK_ANSWER

    if answer == FALLBACK_ANSWER:
        final_answer = answer
    else:
        final_answer = f"{answer}{_source_list(chunks)}"

    return GeneratedAnswer(answer=final_answer, sources=chunks)

def answer_question(question: str, top_k: int = 5) -> str:
    """Retrieve context and return a grounded answer for a user question."""
    chunks = retrieve(question, top_k=top_k)
    return generate_answer(question, chunks).answer

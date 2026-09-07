"""Command-line interface for the Howard study-spots generation pipeline."""

from __future__ import annotations

import argparse


def ask(question: str, top_k: int) -> None:
    """Print one grounded answer, including its source list."""
    try:
        from generate import answer_question

        print(f"\n{answer_question(question, top_k=top_k)}\n")
    except (RuntimeError, ValueError) as error:
        print(f"\nError: {error}\n")


def interactive(top_k: int) -> None:
    """Keep accepting questions until the user enters quit or EOF."""
    print("Howard Study Spots Guide")
    print("Ask about study locations on Howard's campus or around DC.")
    print("Enter 'quit' or press Ctrl+C to exit.\n")

    while True:
        try:
            question = input("Question: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return

        if question.lower() in {"quit", "exit"}:
            print("Goodbye.")
            return
        if not question:
            print("Please enter a question.\n")
            continue
        ask(question, top_k)


def main() -> None:
    """Run one question or launch the interactive query interface."""
    parser = argparse.ArgumentParser(
        description="Ask grounded questions about Howard and DC study spots."
    )
    parser.add_argument(
        "--question",
        help="Ask one question and exit; omit this flag for interactive mode.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of retrieved context chunks to use (default: 5).",
    )
    arguments = parser.parse_args()

    if arguments.top_k < 1:
        parser.error("--top-k must be at least 1")
    if arguments.question:
        ask(arguments.question, arguments.top_k)
    else:
        interactive(arguments.top_k)


if __name__ == "__main__":
    main()

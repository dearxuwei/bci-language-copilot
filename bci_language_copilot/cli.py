from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

from bci_language_copilot.decoder.mock import MockBCIDecoder
from bci_language_copilot.language.phrase_bank import PhraseBankPredictor
from bci_language_copilot.pipeline import CommunicationPipeline

app = typer.Typer(help="BCI-Language Copilot research prototype.")
console = Console()


@app.callback()
def main() -> None:
    """Command group for BCI-Language Copilot."""


@app.command()
def demo(context: str = "clinical", top_k: int = 3) -> None:
    """Run a mock BCI predictive communication demo."""
    pipeline = CommunicationPipeline(decoder=MockBCIDecoder(), predictor=PhraseBankPredictor())
    result = pipeline.run(partial="water", context=context, top_k=top_k)

    table = Table(title="BCI-Language Copilot Demo")
    table.add_column("Rank")
    table.add_column("Decoder Candidate")
    table.add_column("Probability")
    table.add_column("Language Suggestion")

    for index, suggestion in enumerate(result.suggestions, start=1):
        candidate = result.decoded[index - 1] if index - 1 < len(result.decoded) else result.decoded[-1]
        table.add_row(
            str(index),
            candidate.label,
            f"{candidate.probability:.2f}",
            suggestion.text,
        )

    console.print(table)
    console.print(
        f"Stopping decision: {result.stopping.reason} "
        f"(confidence={result.stopping.confidence:.2f})"
    )
    console.print(
        f"Keystroke saving rate: {result.efficiency.keystroke_saving_rate:.2%} "
        f"({result.efficiency.characters_saved} chars saved)"
    )


if __name__ == "__main__":
    app()

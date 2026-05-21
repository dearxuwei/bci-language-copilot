from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

from bci_language_copilot.decoder.mock import MockBCIDecoder
from bci_language_copilot.language.phrase_bank import PhraseBankPredictor
from bci_language_copilot.metrics.input_efficiency import compute_efficiency

app = typer.Typer(help="BCI-Language Copilot research prototype.")
console = Console()


@app.command()
def demo(context: str = "clinical", top_k: int = 3) -> None:
    """Run a mock BCI predictive communication demo."""
    decoder = MockBCIDecoder()
    predictor = PhraseBankPredictor()

    decoded = decoder.predict(partial="water")
    suggestions = predictor.suggest(partial="water", context=context, top_k=top_k)
    metrics = compute_efficiency(selected_text="water", completed_text=suggestions[0].text)

    table = Table(title="BCI-Language Copilot Demo")
    table.add_column("Rank")
    table.add_column("Decoder Candidate")
    table.add_column("Probability")
    table.add_column("Language Suggestion")

    for index, suggestion in enumerate(suggestions, start=1):
        candidate = decoded[index - 1] if index - 1 < len(decoded) else decoded[-1]
        table.add_row(
            str(index),
            candidate.label,
            f"{candidate.probability:.2f}",
            suggestion.text,
        )

    console.print(table)
    console.print(
        f"Keystroke saving rate: {metrics.keystroke_saving_rate:.2%} "
        f"({metrics.characters_saved} chars saved)"
    )


if __name__ == "__main__":
    app()

from __future__ import annotations

from typing import Protocol

from bci_language_copilot.language.phrase_bank import PhraseSuggestion


class LanguagePredictor(Protocol):
    """Rank phrase completions from partial text and context."""

    def suggest(self, partial: str, context: str = "clinical", top_k: int = 3) -> list[PhraseSuggestion]:
        """Return ranked phrase suggestions."""

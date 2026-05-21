from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PhraseSuggestion:
    text: str
    source: str
    score: float


class PhraseBankPredictor:
    """Constrained phrase predictor for safe assistive communication prototypes."""

    _phrases = {
        "clinical": [
            "I need some water.",
            "I am feeling pain and need help.",
            "Please adjust my position.",
            "I need to rest for a while.",
        ],
        "daily": [
            "I would like to talk with my family.",
            "Please help me open the window.",
            "I want to listen to music.",
        ],
        "research": [
            "Please start the next trial.",
            "I need a short break before continuing.",
            "The stimulus is too bright.",
        ],
    }

    def suggest(self, partial: str, context: str = "clinical", top_k: int = 3) -> list[PhraseSuggestion]:
        phrases = self._phrases.get(context, self._phrases["clinical"])
        query = partial.lower().strip()
        ranked = sorted(
            phrases,
            key=lambda phrase: (query not in phrase.lower(), len(phrase)),
        )
        return [
            PhraseSuggestion(text=phrase, source="phrase_bank", score=1.0 / rank)
            for rank, phrase in enumerate(ranked[:top_k], start=1)
        ]

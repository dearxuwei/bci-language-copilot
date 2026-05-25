from __future__ import annotations

from bci_language_copilot.decoder.base import DecodedCandidate


class MockBCIDecoder:
    """Deterministic decoder used for UI and metric development."""

    def predict(self, partial: str = "") -> list[DecodedCandidate]:
        labels = [partial or "help", "pain", "rest"]
        probabilities = [0.72, 0.18, 0.10]
        if len(labels) != len(probabilities):
            raise ValueError("labels and probabilities must have the same length")
        return [
            DecodedCandidate(label=label, probability=probability)
            for label, probability in zip(labels, probabilities)
        ]

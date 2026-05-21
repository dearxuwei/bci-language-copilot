from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class DecodedCandidate:
    label: str
    probability: float


class BCIDecoder(Protocol):
    def predict(self, partial: str = "") -> list[DecodedCandidate]:
        """Return ranked candidates from EEG or simulated input."""

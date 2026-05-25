from __future__ import annotations

from dataclasses import dataclass

from bci_language_copilot.decoder.base import DecodedCandidate


@dataclass(frozen=True)
class StoppingDecision:
    should_stop: bool
    reason: str
    confidence: float


@dataclass(frozen=True)
class AdaptiveStoppingPolicy:
    """Simple confidence gate inspired by adaptive stopping in P300 spellers."""

    confidence_threshold: float = 0.70
    min_margin: float = 0.20

    def decide(self, candidates: list[DecodedCandidate]) -> StoppingDecision:
        if not candidates:
            return StoppingDecision(False, "no candidates", 0.0)
        ranked = sorted(candidates, key=lambda item: item.probability, reverse=True)
        top = ranked[0]
        runner_up = ranked[1].probability if len(ranked) > 1 else 0.0
        margin = top.probability - runner_up
        should_stop = top.probability >= self.confidence_threshold and margin >= self.min_margin
        reason = "confidence threshold met" if should_stop else "collect more evidence"
        return StoppingDecision(should_stop, reason, top.probability)

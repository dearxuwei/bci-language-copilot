from __future__ import annotations

from dataclasses import dataclass

from bci_language_copilot.decoder.base import BCIDecoder, DecodedCandidate
from bci_language_copilot.language.base import LanguagePredictor
from bci_language_copilot.language.phrase_bank import PhraseSuggestion
from bci_language_copilot.metrics.input_efficiency import InputEfficiency, compute_efficiency
from bci_language_copilot.stopping import AdaptiveStoppingPolicy, StoppingDecision


@dataclass(frozen=True)
class CommunicationResult:
    decoded: list[DecodedCandidate]
    suggestions: list[PhraseSuggestion]
    stopping: StoppingDecision
    efficiency: InputEfficiency


@dataclass(frozen=True)
class CommunicationPipeline:
    """Coordinate BCI decoding, stopping, language ranking, and efficiency accounting."""

    decoder: BCIDecoder
    predictor: LanguagePredictor
    stopping_policy: AdaptiveStoppingPolicy = AdaptiveStoppingPolicy()

    def run(self, partial: str, context: str = "clinical", top_k: int = 3) -> CommunicationResult:
        decoded = self.decoder.predict(partial=partial)
        stopping = self.stopping_policy.decide(decoded)
        suggestions = self.predictor.suggest(partial=partial, context=context, top_k=top_k)
        completed_text = suggestions[0].text if suggestions else partial
        efficiency = compute_efficiency(selected_text=partial, completed_text=completed_text)
        return CommunicationResult(
            decoded=decoded,
            suggestions=suggestions,
            stopping=stopping,
            efficiency=efficiency,
        )

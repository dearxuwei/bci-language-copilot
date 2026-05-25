from bci_language_copilot.decoder.mock import MockBCIDecoder
from bci_language_copilot.language.phrase_bank import PhraseBankPredictor
from bci_language_copilot.pipeline import CommunicationPipeline
from bci_language_copilot.stopping import AdaptiveStoppingPolicy


def test_pipeline_returns_decoding_language_and_efficiency() -> None:
    pipeline = CommunicationPipeline(decoder=MockBCIDecoder(), predictor=PhraseBankPredictor())

    result = pipeline.run(partial="water", context="clinical", top_k=3)

    assert result.decoded[0].label == "water"
    assert result.suggestions[0].text == "I need some water."
    assert result.efficiency.characters_saved == 13
    assert result.stopping.should_stop is True


def test_stopping_policy_requires_margin() -> None:
    pipeline = CommunicationPipeline(
        decoder=MockBCIDecoder(),
        predictor=PhraseBankPredictor(),
        stopping_policy=AdaptiveStoppingPolicy(confidence_threshold=0.8),
    )

    result = pipeline.run(partial="water")

    assert result.stopping.should_stop is False

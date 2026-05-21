from bci_language_copilot.language.phrase_bank import PhraseBankPredictor


def test_phrase_bank_returns_suggestions() -> None:
    suggestions = PhraseBankPredictor().suggest("water", top_k=2)

    assert len(suggestions) == 2
    assert "water" in suggestions[0].text.lower()

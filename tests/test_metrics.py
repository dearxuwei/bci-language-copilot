from bci_language_copilot.metrics.input_efficiency import compute_efficiency


def test_compute_efficiency() -> None:
    metrics = compute_efficiency("water", "I need some water.")

    assert metrics.characters_saved > 0
    assert 0 < metrics.keystroke_saving_rate < 1

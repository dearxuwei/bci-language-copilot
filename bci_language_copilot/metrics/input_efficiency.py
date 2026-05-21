from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class InputEfficiency:
    selected_characters: int
    completed_characters: int
    characters_saved: int
    keystroke_saving_rate: float


def compute_efficiency(selected_text: str, completed_text: str) -> InputEfficiency:
    selected = len(selected_text)
    completed = len(completed_text)
    saved = max(completed - selected, 0)
    rate = saved / completed if completed else 0.0
    return InputEfficiency(
        selected_characters=selected,
        completed_characters=completed,
        characters_saved=saved,
        keystroke_saving_rate=rate,
    )

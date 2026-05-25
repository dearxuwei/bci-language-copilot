# Reading Notes for Promotional Visuals

## Downloaded Local Papers

- `papers/ChatBCI_SciRep_2026_PMC12909297.html`
- `papers/ChatBCI_Assist_TBME_2026_pubmed.html`

## Paper 1: ChatBCI, Scientific Reports, 2026

Source: Hong J, Wang W, Najafizadeh L. *Scientific Reports*. DOI: `10.1038/s41598-025-25660-7`.

### Methods Worth Reflecting in Visuals

- P300 speller BCI with an LLM-integrated graphical keyboard.
- EEG is streamed and classified for P300 detection using SWLDA.
- Selected keys update a GUI that includes normal character keys plus LLM-generated word candidates.
- GPT-3.5 is queried for word completion and next-word or multi-word prediction.
- The paper frames predictive typing using keystroke analysis, not only character-level BCI metrics.

### Results Worth Reflecting in Visuals

- In copy-spelling, ChatBCI reported average reductions of `62.14%` in completion time and `53.22%` in keystrokes compared with letter-by-letter spelling.
- The reported information transfer rate increased by `229.48%`.
- In improvised spelling, reported keystroke savings averaged `80.68%`.
- The paper reports that multi-word suggestions sometimes allowed phrase-level selection in a single attempt.

### Design Translation

Use a visual chain:

`P300 neural response -> keyboard/selector -> LLM candidate manifold -> phrase-level output`

Include small evidence labels:

- `53.22% fewer keystrokes`
- `80.68% KS in improvisation`
- `+229.48% ITR`

These labels should be explicitly framed as prior-work evidence/inspiration, not as results from this repository.

## Paper 2: ChatBCI-Assist, IEEE TBME, 2026

Source: Hong J, Rao P, Wang W, et al. *IEEE Transactions on Biomedical Engineering*. DOI: `10.1109/TBME.2026.3693965`.

### Methods Worth Reflecting in Visuals

- Intent-based P300 spelling.
- Locally deployed LLM.
- Adaptive stopping strategy.

### Design Translation

Visual emphasis:

- local AI node rather than only cloud AI
- adaptive confidence/stopping ring around the selector
- intent-level phrase completion instead of character-by-character typing

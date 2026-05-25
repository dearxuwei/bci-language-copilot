# Literature Map: BCI-Language Copilot

This file records papers that motivate the BCI-Language Copilot visual and technical direction. Do not vendor copyrighted PDFs here; keep links, metadata, and concise design notes.

## Core Papers

1. Hong J, Wang W, Najafizadeh L. **ChatBCI, a P300 speller BCI with context-driven word prediction leveraging large language models, from concept to evaluation.** *Scientific Reports*. 2026. DOI: `10.1038/s41598-025-25660-7`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/41698950/
   - PMC: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12909297/
   - Project relevance: closest prior art for P300 spelling + context-driven LLM word prediction.
   - Visual cues to borrow: matrix speller, intent candidates, language-model completion path, human-centered assistive loop.

2. Hong J, Rao P, Wang W, et al. **ChatBCI-Assist: An Intent-Based P300 Speller with A Locally-Deployed LLM and Adaptive Stopping Strategy Enabling Record Online Spelling Performance.** *IEEE Transactions on Biomedical Engineering*. 2026. DOI: `10.1109/TBME.2026.3693965`.
   - PubMed: https://pubmed.ncbi.nlm.nih.gov/42139128/
   - Project relevance: intent-based P300 spelling, local LLM, adaptive stopping.
   - Visual cues to borrow: online closed-loop system, local AI node, adaptive stopping/decision confidence.

## Visual Translation

The cover image should avoid looking like a generic chatbot. It should foreground:

- a human brain/head silhouette with EEG electrodes
- a P300 spelling grid or target-selection field
- a luminous path from neural signal to language candidates
- a local AI/language module as an abstract transformer/semantic field
- a final assistive phrase, but with minimal text

## Avoid

- generic robot faces
- ordinary chat bubbles as the main subject
- dense UI screenshots
- cartoonish brain icons
- medical-device claims

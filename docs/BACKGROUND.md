# Background

BCI communication systems such as P300 and SSVEP spellers can help users select characters, commands, or phrase candidates. However, direct character-by-character input is slow and cognitively demanding. Language prediction can reduce the number of required selections by using context, phrase banks, and language models to propose complete expressions.

This project focuses on the intersection of:

- EEG-based BCI intent decoding
- assistive communication
- predictive text input
- human-AI interaction
- transparent evaluation of interaction efficiency

The month-1 objective is not a clinical product. It is a reproducible application prototype that demonstrates how BCI probabilities and language prediction can form a useful communication loop.

## Design Principles

- Start with mock and offline modes before live hardware.
- Keep all safety-critical communication claims conservative.
- Log interaction metrics so progress can be measured.
- Prefer phrase-constrained prediction for sensitive assistive contexts.
- Make every decoder and language provider replaceable.

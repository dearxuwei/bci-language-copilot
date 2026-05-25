# Technical Plan

## Architecture

```text
EEG epoch / simulated probabilities
-> decoder posterior over symbols or intents
-> adaptive stopping policy
-> context-aware phrase predictor
-> ranked phrase output
-> input-efficiency and safety report
```

## Modules

- `decoder`: converts EEG or simulated input into ranked symbols/intents.
- `stopping`: decides whether candidate confidence is sufficient or more evidence is needed.
- `language`: completes phrases from selected partial input and context.
- `pipeline`: coordinates decoder, stopping, language prediction, and efficiency accounting.
- `metrics`: measures interaction efficiency.
- `ui`: future Streamlit/web interface.

## Research Pain Points

| Pain Point | Why It Matters | Current Open-Source Route |
|---|---|---|
| Low BCI bandwidth | Character-level spelling is slow and error-prone. | Phrase-level completion from sparse decoded intent. |
| Unclear stopping logic | Over-collecting EEG trials slows communication; stopping too early increases errors. | `AdaptiveStoppingPolicy` exposes threshold and margin. |
| Language model opacity | LLM assistance can become a black-box UI feature. | `LanguagePredictor` protocol separates phrase bank and future local LLM providers. |
| Weak efficiency reporting | Many demos show output but not interaction cost. | `InputEfficiency` reports selected, completed, saved characters, and saving rate. |
| Safety overclaiming | Assistive BCI prototypes must not imply emergency reliability. | Safety boundary is part of docs, CLI language, and figure design. |

## Algorithmic Route

1. Decode a candidate list from EEG or simulated evidence.
2. Sort candidates by posterior probability.
3. Apply adaptive stopping with a confidence threshold and top-2 margin.
4. Use partial text and context to rank phrase suggestions.
5. Report selected characters, completed characters, characters saved, and keystroke saving rate.
6. Keep the clinical boundary explicit: this is a research prototype, not a medical or emergency communication device.

## Initial Metrics

- `selection_count`: number of BCI selections needed.
- `characters_saved`: generated characters minus selected characters.
- `keystroke_saving_rate`: saved characters divided by generated characters.
- `top_k_contains_target`: whether the intended phrase appears in the top-k candidates.

## Interpreter

Target local interpreter:

```text
D:\AI_Env\dl_5060ti\python.exe
```

The repository avoids committing virtual environments. Recreate dependencies from `pyproject.toml`.

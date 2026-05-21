# Technical Plan

## Architecture

```text
BCI signal or simulated probabilities
-> decoder
-> candidate selector
-> language predictor
-> communication UI
-> metrics logger
```

## Modules

- `decoder`: converts EEG or simulated input into ranked symbols/intents.
- `language`: completes phrases from selected partial input and context.
- `metrics`: measures interaction efficiency.
- `ui`: future Streamlit/web interface.

## Initial Metrics

- `selection_count`: number of BCI selections needed.
- `characters_saved`: generated characters minus selected characters.
- `keystroke_saving_rate`: saved characters divided by generated characters.
- `top_k_contains_target`: whether the intended phrase appears in the top-k candidates.

## Interpreter

Target local interpreter:

```text
D:\AI_Env\dl_5060ti\Scripts\python.exe
```

The repository avoids committing virtual environments. Recreate dependencies from `pyproject.toml`.

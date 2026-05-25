# Mac Setup

This project uses the Mac system Python directly. Do not create a `.venv`, Conda environment, Poetry environment, or uv environment for normal local development.

## Tools

Check the required tools:

```bash
git --version
gh --version
python3 --version
python3 -m pip --version
```

If `git`, `gh`, or a suitable `python3` is missing, install Homebrew first, then install the missing tools:

```bash
brew install git gh python
```

Log in to GitHub when push access is needed:

```bash
gh auth login
```

Choose GitHub.com, HTTPS, and browser login.

## Clone

```bash
mkdir -p ~/AI_OpenSource
cd ~/AI_OpenSource
git clone https://github.com/dearxuwei/bci-language-copilot.git
cd bci-language-copilot
```

Before starting work on an existing checkout:

```bash
git pull --ff-only
```

## Install

Use system Python:

```bash
python3 -m pip install -U pip setuptools wheel
python3 -m pip install -e ".[dev]"
```

If macOS reports an externally managed Python environment or blocks global installs, use the user site:

```bash
python3 -m pip install --user -U pip setuptools wheel
python3 -m pip install --user -e ".[dev]"
```

## VS Code Or Cursor

Keep `.vscode/settings.json` local and untracked. Copy `.vscode/settings.example.json` if useful, then point it at the Mac Python path from:

```bash
which python3
```

Example:

```json
{
  "python.defaultInterpreterPath": "/usr/bin/python3",
  "python.terminal.activateEnvironment": false
}
```

## Verify

```bash
python3 -m pytest -q
python3 -m bci_language_copilot.cli demo
```

## Commit And Push

```bash
git status
git add .
git commit -m "your commit message"
git push
```

# Windows Setup

Windows development should continue to use the existing interpreter:

```text
D:\AI_Env\dl_5060ti\python.exe
```

Do not sync Python environments between Windows and Mac. Sync only code, documentation, tests, and configuration templates through GitHub.

## Clone Or Update

```powershell
mkdir $HOME\AI_OpenSource
cd $HOME\AI_OpenSource
git clone https://github.com/dearxuwei/bci-language-copilot.git
cd bci-language-copilot
git pull --ff-only
```

## Install

```powershell
D:\AI_Env\dl_5060ti\python.exe -m pip install -U pip setuptools wheel
D:\AI_Env\dl_5060ti\python.exe -m pip install -e ".[dev]"
```

## VS Code Or Cursor

Keep `.vscode/settings.json` local and untracked. Windows users can point it at the Windows interpreter:

```json
{
  "python.defaultInterpreterPath": "D:\\AI_Env\\dl_5060ti\\python.exe",
  "python.terminal.activateEnvironment": false
}
```

## Verify

```powershell
D:\AI_Env\dl_5060ti\python.exe -m pytest -q
D:\AI_Env\dl_5060ti\python.exe -m bci_language_copilot.cli demo
```

## Sync With Mac

Start work:

```powershell
git pull --ff-only
```

Review changes:

```powershell
git status
```

Commit and push:

```powershell
git add .
git commit -m "your commit message"
git push
```

On the other computer, pull before continuing:

```powershell
git pull --ff-only
```

# stock-watcher

## Purpose of the project
It's for self study. All the code is hand-written. AI is only used for review and explanations.

## What it does
Right now it's only a parser with 'hello' command, that prints 'hello'. At the end will be able to watch stocks and report changes.

## Status
'hello' command works. Planning 'report', 'watch', 'alert' commands.

## Requirements
Python version 3.12 or later.  
```
winget install --id Git.Git -e  
winget install --id astral-sh.uv -e  
```

## How to run
```
git clone https://github.com/emiru128-sys/stock-watcher  
cd stock-watcher  
uv run stock-watcher hello
```
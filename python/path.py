from pathlib import Path
entries = Path('.')
for entry in entries.iterdir():
    print(entry.name)

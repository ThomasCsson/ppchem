from pathlib import Path

p = Path('.')

print(p.resolve())

for file in p.iterdir():
    print(file)

new_dir = p / 'new_directory'

new_dir.mkdir(exist_ok=True)


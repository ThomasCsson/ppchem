from pathlib import Path

p = Path('.')

print(p.resolve())

for file in p.iterdir():
    print(file)

new_dir = p / 'new_directory'

new_dir.mkdir(exist_ok=True)

print(new_dir.exists())

new_file = new_dir / 'new_file.txt'
new_file.touch()

print(new_file.exists())

new_file.unlink()

print(new_file.exists())

new_dir.rmdir()

print(new_dir.exists())


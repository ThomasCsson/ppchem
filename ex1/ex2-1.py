from pathlib import Path

p = Path('.')

print(p.resolve())

new_dir = p / 'ex_folder'
new_dir.mkdir(exist_ok=True)

print(new_dir.exists())

new_file = new_dir / 'ex_file.txt'
new_file.touch()

print(new_file.exists())

new_file.unlink()

new_dir.rmdir()
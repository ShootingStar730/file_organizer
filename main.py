from pathlib import Path
import sys

path = Path(sys.argv[1])
# print(path)

for item in path.iterdir():
    if item.is_file():
        extension = item.suffix[1:]

        folder = path / extension
        folder.mkdir(exist_ok=True)

        destination = folder / item.name

        item.rename(destination)



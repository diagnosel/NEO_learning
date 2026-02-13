from pathlib import Path

def parse_folder(path):
    for el in path.iterdir():
        if el.is_file():
            print(f'{el} is a file')
        elif el.is_dir():
            print(f'{el} is a folder')
        else:
            print(f'{el} is something else')
            
parse_folder(Path("."))

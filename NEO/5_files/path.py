from pathlib import PurePath, Path

# p = PurePath("/usr/bin/simple.jpg")
# print("Name:", p.name)  
# print("Suffix:", p.suffix) 
# print("Parent:", p.parent)


# p = Path("example.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) 
# print("Exists:", p.exists()) 


# # Початковий шлях
# base_path = Path("/usr/bin")

# # Додавання додаткових частин до шляху
# full_path = base_path / "subdir" / "script.py"

# print(full_path)  # Виведе: /usr/bin/subdir/script.py





# Створення об'єкту Path для директорії
directory = Path("./5_files")

# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)
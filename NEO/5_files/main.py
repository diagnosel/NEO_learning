import json
from fake_user_generator import generate_fake_data

filename = input("Enter the filename: ")
amount = int(input("Enter the amount of lines to read: "))


print(__name__)

with open(filename, "w", encoding="utf-8") as file:
    users = []
    for _ in range(amount):
        users.append(generate_fake_data())
    json.dump(users, file, ensure_ascii=False, indent=2)
        
    
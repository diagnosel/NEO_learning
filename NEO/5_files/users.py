users = []

# with open("users.txt", "w") as file:
#     file = open("users.txt", "w")
#     age = 30
#     info = "Nina " + str(age)
#     file.write(info + "\n")
#     file.write("Alice\n")
#     file.write("Bob\n")

# with open("users.txt", "w") as file:
#     file.writelines(["Nina2\n", "Alice2\n", "Bob2\n"])
#     print(file.tell())


with open("image.png", "rb") as file:
    image_bin = file.read()
    print(image_bin)
    print(type(image_bin))
f = open("hello.txt", "r")
#1
data = f.read()
print(data)
f.close()


f = open("hello.txt", "r")
#2
print("lines\n")
lines = f.readlines()
print(lines)
f.close()
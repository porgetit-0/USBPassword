from random import choice
import string

# print(choice(string.ascii_letters))

password = []

for i in range(0, 100):
    password.append(choice(string.ascii_letters))

password = "".join(password)

file = open("password.txt", "a")
file.write(password)
file.close()
# 1
name = input("Whats your name? ")
print(f"Hello, {name}")


# 2
names = []

for _ in range(3):
    name = input("Whats your name? ")
    names.append(name)

print(f"Hello, {names}")


# 3
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f'Hello, {name}')


# storing Information

# open : opens a file in order to read or write
# w = write. It will rewrite the whole file everytime
# 4
name = input("Whats your name? ")

file = open("names.txt", 'w')
file.write(name)
file.close()


# 5
# a = append. It will append the data each time with the previous data.
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()


# 6
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


# 7
# with
name = input("What's your name? ")

with open("names.txt", "a") as file :
    file.write(f"{name}\n")


# 8
r = read. Reads a file.
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello", line)


# 9
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello", line.strip())


# 10
with open("names.txt", "r") as file:
    for line in file:
        print("Hello", line.rstrip())


# 11
names = []
# opens the file, reads all the datas and sort them.
with open("names.txt") as file:
    for line in file:
        names. append(line.rstrip())
# print the sorted datas
for name in sorted(names):
    print(f"Hello {name}")


# 12
with open("names.txt") as file:
    for line in sorted(file):
        print("Hello", line.rstrip())

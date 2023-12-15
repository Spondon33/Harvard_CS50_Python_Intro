#1 Cat
print("meow")
print("meow")
print("meow")


#2 while loop
i = 3
while i != 0:
    print("meow")
    i = i - 1


#3
i = 1
while i <= 3:
    print("meow")
    i = i + 1


#4 start from 0 instead of 1
i = 0
while i < 3:
    print("meow")
    i = i + 1


#5 i + 1 is written as += 1
i = 0
while i < 3:
    print("meow")
    i += 1


# for loop

#1
for i in [0, 1, 2]:
    print("meow")


#2 sets a range of values
# we can write _ insted of i as i is not used as a variable
for _ in range(3):
    print("meow")


#3 will show meowmeowmeow
print("meow" * 3)


#4 \n prints each meow in seperate lines
print("meow\n" * 3)


#5 removes the default end at the end
print("meow\n" * 3, end = "")


#6
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break


#7
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


#8 defines a new meow function
def main():
    meow(3)


def meow(n):
    for _ in range(n):
        print("meow")


main()


#9
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()


# Hogwarts

#1 List
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])


#2
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)


#3
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])


# Dictionaries or dict

#1
students= {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


#2 for loop will only show the keys
students= {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student)


#3 will print the houses too
students= {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=", ")


#4 list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronous": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronous": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronous": None}
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")
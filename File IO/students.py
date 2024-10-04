# # 1
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
#
# # 2
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
#
# # 3
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)
#
# # 4
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)
#
# for student in students:
#     print(f"{student['name']} is in {student['house']}")
#
# # 5
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
# for student in students:
#     print(f"{student['name']} is in {student['house']}")
#
# # 6
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# def get_name(student):
#     return student["name"]
#
#
# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")
#
# # 7
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# def get_name(student):
#     return student["name"]
#
#
# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")
#
# # 8
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# def get_house(student):
#     return student["house"]
#
#
# for student in sorted(students, key=get_house):
#     print(f"{student['name']} is in {student['house']}")
#
# # 9
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")
#
# # 10
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, home = line.strip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
#
# # 11
# import csv
#
# students = []
#
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# 12
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

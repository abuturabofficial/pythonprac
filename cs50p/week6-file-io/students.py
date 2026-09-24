# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")


# # Students Sorted
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
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


# # Students sorted with lambda function
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")


# # Students sorted (with home addresses)
# students = []
# with open("students_homes.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)
#
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from{student['home']}")


# # Using CSV module
# import csv
# students = []
# with open("students_homes.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# # Using CSV module: DICTREADER
# import csv
# students = []
# with open("students_homes.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# # Using CSV moduel: appending to a file via Writer
# import csv
# name = input("What's your name? ")
# home = input("Where is your home? ")
#
# with open("students_homes.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])


# using csv module: appednign to a file via DictWriter
import csv
name = input("What's your name? ")
home = input("Where is your home? ")

with open("students_homes.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

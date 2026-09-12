# Students with their houses names dictionary values
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# # Print each student's hosue name
# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])


# Print students' name and house
for student in students:
    print(student, students[student], sep=", ")

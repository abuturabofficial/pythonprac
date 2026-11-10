# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
#
#
# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
#
#
# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# # list compreh
# gryffindors = [{"name": student, "house": "Gryffindor"}
#                for student in students]
# print(gryffindors)

# dict compreh
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)

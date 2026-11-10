students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])


for i, student in enumerate(students, start=1):
    print(i, student)  # for no start value 'print(i + 1, student)'

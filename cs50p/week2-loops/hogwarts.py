students = ["Hermione", "Harry", "Ron"]

# # Print each student via index number
# print(students[0])
# print(students[1])
# print(students[2])


# # more succinct approach would be
# for student in students:
#     print(student)


# print students names using len() function
for i in range(len(students)):
    print(i + 1, students[i])


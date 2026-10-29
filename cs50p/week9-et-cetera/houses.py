students = [
    {"Name": "Hermione", "House": "Gryffindor"},
    {"Name": "Harry", "House": "Gryffindor"},
    {"Name": "Ron", "House": "Gryffindor"},
    {"Name": "Draco", "House": "Slytherin"},
    {"Name": "Padma", "House": "Ravenclaw"}
]

houses = []
for student in students:
    if student["House"] not in houses:
        houses.append(student["House"])

for house in sorted(houses):
    print(house)

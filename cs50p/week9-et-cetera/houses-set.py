students = [
    {"Name": "Hermione", "House": "Gryffindor"},
    {"Name": "Harry", "House": "Gryffindor"},
    {"Name": "Ron", "House": "Gryffindor"},
    {"Name": "Draco", "House": "Slytherin"},
    {"Name": "Padma", "House": "Ravenclaw"}
]

houses = set()
for student in students:
    houses.add(student["House"])
for house in sorted(houses):
    print(house)

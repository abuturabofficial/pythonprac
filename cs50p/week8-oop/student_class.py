class Student():
    def __init__(self, name, house):
        self.name = name
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Slytherin", "RavenClaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house}."


def main():
    student = get_student()
    # print(f"{student.name} is from {student.house}.")
    print(student)


def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
    # return student


if __name__ == "__main__":
    main()

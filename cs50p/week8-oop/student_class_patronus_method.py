class Student():
    def __init__(self, name, house, patronus):
        self.name = name
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Slytherin", "RavenClaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} is from {self.house}."

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    # print(f"{student.name} is from {student.house}.")
    print(student)
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)
    # return student


if __name__ == "__main__":
    main()

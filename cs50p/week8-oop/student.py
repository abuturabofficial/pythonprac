def main():
    # name, house = get_student()
    # print(f"{name} is from {house}.")
    student = get_student()
    print(f"{student[0]} is from {student[1]}.")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # return immutabe tuple
    return (name, house)


if __name__ == "__main__":
    main()

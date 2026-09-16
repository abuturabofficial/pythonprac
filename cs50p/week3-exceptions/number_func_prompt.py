# let's user decide which prompt to use
def main():
    x = get_int("What's the value of x: ")
    print(f"The value of x is: {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer.")
main()

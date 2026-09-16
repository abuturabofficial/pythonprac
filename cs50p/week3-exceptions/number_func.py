def main():
    x = get_int()
    print(f"The value of x is: {x}")


def get_int():
    # while True:
    #     try:
    #         x = int(input("What's the value of x: "))
    #     except ValueError:
    #         print("x is not an integer.")
    #     else:
    #         return x

    # efficient
    while True:
        try:
            return int(input("What's the value of x: "))
        except ValueError:
            print("x is not an integer.")



main()

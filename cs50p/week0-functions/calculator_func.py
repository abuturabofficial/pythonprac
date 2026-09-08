def main():
    x = int(input("What's the value of x? "))
    print("The square of x is: ", square(x))


def square(n):
    return pow(n, 2)

main()

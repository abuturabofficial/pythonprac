# Extra Project from book's chapter 3

def collatz(number):
    if number % 2 == 0:
        result = int(number / 2)
    else:
        result = int(3 * number + 1)
    print(result)
    return result


try:
    number = int(input("Enter your number:\n"))
    while number != 1:
        number = collatz(number)
except ValueError:
    print('Please enter a valid integer')

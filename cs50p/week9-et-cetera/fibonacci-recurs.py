'''
The Fibonacci Sequence is the series of numbers:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]
The next number is found by adding up the two numbers before it:
'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


try:
    # Get fibonacci sequence till the ipnut-->ask number.
    ask = int(input("What's your number? "))
    fseq = []
    for i in range(ask+1):
        if fibonacci(i) > ask:  # Stop fibonacci seq past input-->ask value
            break
        fseq.append(fibonacci(i))

    print("Fibonacci Seq:", fseq)

    # # Get fibonacci number at the position input-->ask
    # print(f"{ask} Fibonacci Number: {fibonacci(ask)}")
except ValueError:
    print("Only Integers are allowed.")

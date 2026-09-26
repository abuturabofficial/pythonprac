def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return (f'Error: I cannot do 42/{divideBy}.')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

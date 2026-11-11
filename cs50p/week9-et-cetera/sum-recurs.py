'''
Write a recursive function to calculate the sum of first n natural numbers ---Shradha Khapra
'''


def sum_num(n):
    if n == 1:
        return 1
    return n + sum_num(n - 1)


print(sum_num(100))

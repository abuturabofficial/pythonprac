'''
Recursion: Countdown numbers backward from the given starting value. ---Shradha Khapra
'''


def countdown(n):
    if n < 0:
        return
    else:
        print(n)
        return countdown(n - 1)


countdown(15)

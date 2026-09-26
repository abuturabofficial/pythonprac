import sys
import time


def asterisks_pattern(startSpace, pattern):
    print(' ' * startSpace + pattern)
    time.sleep(0.1)


pattern = '******'

while True:
    try:
        for startSpace in range(10):
            asterisks_pattern(startSpace, pattern)

        for startSpace in range(10, 1, -1):
            asterisks_pattern(startSpace, pattern)
    except KeyboardInterrupt:
        print(' Quiting the animation pattern. Goodbye!')
        sys.exit()

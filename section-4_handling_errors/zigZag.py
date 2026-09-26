import sys
import time

while True:
    try:
        for startSpace in range(10):
            print(' ' * startSpace, end='')
            print('******')
            startSpace = startSpace + 1
            time.sleep(0.1)

        for startSpace in range(10, 1, -1):
            print(' ' * startSpace, end='')
            print('******')
            time.sleep(0.1)
            startSpace = startSpace - 1
    except KeyboardInterrupt:
        print(' Quiting the animation pattern. Goodbye!')
        sys.exit()

def main():
    height = int(input("Height: "))
    pyramid (height)

"""
I have used ZED debugger to find out that first value assigned to i = 0, which when multiplied, it gives 0 number of tiles in the first run. To fix it when need to start from 1
"""
def pyramid(n):
    for i in range(n):
        print ("#" * (i + 1))

if __name__ == "__main__":
    main()

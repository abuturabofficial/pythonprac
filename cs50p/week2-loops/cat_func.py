def main():
    num = get_num()
    meow(num)

def meow(n):
    for _ in range(n):
        print("meow")

def get_num():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


main()

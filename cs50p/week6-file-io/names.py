# names = []
#
# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)
#
# for name in sorted(names):
#     print(f"hello, {name}")


# # Using File I/O --- Write
# name = input("What's your name? ")
#
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# # Using File I/O --- Read
# with open("names.txt", "r") as file:
#     lines = file.readlines()
#
# for line in lines:
#     print("hello,", line.rstrip())


# # More Pythonic way of Read
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())


# Read: But sorted
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print("hello,", name)

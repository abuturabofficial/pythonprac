### While Loops ###

# i = 3
# while i != 0:
#     print(i, "meow")
#     i = i - 1


# # Count upward
# i = 1
# while i <= 3:
#     print(i, "meow")
#     i = i + 1


# # Programmers count from zero
# i = 0
# while i < 3:
#     print(i, "meow")
#     i += 1 #more efficient syntax to say i = i + 1


### For Loops ###

# # Using for loop and a list
# for i in (0, 1, 2):
#     print(i, "meow")

# # Using for loop and range() function
# for i in range(3):
#     print(i, "meow")

# # more barebone approach
# print("meow\n" * 3, end="")


# Ask for how many times a cat should meow
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")

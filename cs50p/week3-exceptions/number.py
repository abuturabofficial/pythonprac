# # Value Error when put a string
# x = int(input("What's the value of x: "))
# print(f"The value of x is: {x}")


# # Catch an error
# try:
#     x = int(input("What's the value of x: "))
#     print(f"The value of x is: {x}")
# except ValueError:
#     print("x is not an integer.")


# # Better approach only inlcude necessary code in try-except block
# try:
#     x = int(input("What's the value of x: "))
# except ValueError:
#     print("x is not an integer.")
#
# print(f"The value of x is: {x}") # It introduces NameError when try-except catches ValueError


# # else can be used with try-except block when there is no error
# try:
#     x = int(input("What's the value of x: "))
# except ValueError:
#     print("x is not an integer.")
# else:
#     print(f"The value of x is: {x}")


# let's use a loop to ask user for input until correct value is provided
while True:
    try:
        x = int(input("What's the value of x: "))
    except ValueError:
        print("x is not an integer.")
    else:
        break

print(f"The value of x is: {x}")

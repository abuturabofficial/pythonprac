# # More elaborate Cal
# x = input("What's x? ")
# y = input("What's y? ")
#
# # Convert str to int for summation
# sum = int(x) + int(y)
#
# print(sum)


# # Concise with less lines of code
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# print(x + y)


# # One line but less readable
# print(int(input("What's x? ")) + int(input("What's y? ")))


# # Floats with deicmal point
# x = float(input("What's x? "))
# y = float(input("What's y? "))
#
# # Round to nearest integer
# rounded = round(x+y)
#
# # Add commas for bigger numbers for legibility
# print(f'{rounded:,}')


# Division
x = float(input("What's x? "))
y = float(input("What's y? "))

# # Round to 2 decimal places
# print (round(x/y, 2))

# Round using f-string
print(f'{x/y: .2f}')


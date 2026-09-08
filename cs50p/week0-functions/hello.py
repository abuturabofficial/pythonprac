name = input("What's your name? ")
# print("Hello!", name)

# # Override the end parameter with nothing in-between
# print("Hello! ,", end='')
# print(name)

# # Default separator is a space
# print("Hello,", name, sep='-')

# Using an f-string
# print(f'Hello, {name}')

# Remove white space from string
name = name.strip()

# Capitalize the name
name = name.capitalize()

# Capitalize the both first and last name
name = name.title()

print(f'Hello, {name}')

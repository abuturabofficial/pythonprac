# Ask for username, strip white spaces, titlecase
name = input("What's your name? ").strip().title()

# Greet user with their first name
first, last= name.split(' ')

# Say hello to the user
print(f'Hello, {first}!')

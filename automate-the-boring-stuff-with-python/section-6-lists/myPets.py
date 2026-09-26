mypets = ['Sophie', 'Alice', 'Bob', 'Mona', 'Laura']

petName = input("Type your Pet Name: ").capitalize()

if petName not in mypets:
    print(f"I don't have a pet named {petName}.")
else:
    print(f"{petName} is my pet.")

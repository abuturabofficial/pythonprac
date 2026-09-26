while True:
    print("Who are you?")
    name = input("Enter your name: ")
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (Hint: It is a fish.)")
    password = input("Hi, Joe: Enter the password: ")
    if password == "swordfish":
        break
print("Access Granted: Launching ICBMs")

email = input("What's your email address? ").strip()
username, domain = email.split("@")

if username and domain.endswith(("gmail.com", ".edu")):
    print("Valid")
else:
    print("Invalid")

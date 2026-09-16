# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")


# Choose to raise what kind of exception you want to raise
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

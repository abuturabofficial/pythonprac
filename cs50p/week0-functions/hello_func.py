# Main where all the codes live
def main():
    name = input("What's your name? ")
    hello(name)


# Define as many functions as you want
def hello(to="World!"):
    # Say hello to the user
    print('Hello,', to.strip().title())

# Call main to start executing the main code 
# body which in-turns calls on the defined functions
main()

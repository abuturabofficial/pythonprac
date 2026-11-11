'''
Write a recursive function to print all elements in a list.
Hint: use list & index as parameters. ---Shradha Khapra
'''


def print_items(items, i=0):
    if i == len(items):
        return
    print(items[i])
    print_items(items, i+1)


cities = ["Lahore", "Karachi", "Islamabad",
          "Faisalabad", "Quetta", "Peshawer", "Sibi"]


print_items(cities)

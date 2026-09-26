catName = []

while True:
    print(f"Enter your cat name: {
          len(catName) + 1} (Or Enter nothing to stop.)")
    name = input()
    if name == '':
        break
    catName = catName + [name]


print("The cat names are: ")
for name in catName:
    print(f"  {name}")

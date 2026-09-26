def comaCode(items):
    if len(items) == 0:
        return 'No item is in the list'
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]


userlist = input('Enter items separated by spaces\n').split()

print(comaCode(userlist))

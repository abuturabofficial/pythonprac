### List comprehnsion ###

# list = []
# for i in range(20):
#     if i%2 == 0:
#         list.append(i)
# print(list)
#
# list = []
# even_list = [i for i in range(20) if i%2==0]
# print(even_list)

### Dict comprehnsion ###

dict = {}
for i in range(10):
    if i%2 == 0:
        dict[i] = i ** 2

dict_comp = {i:i**2 for i in range(10) if i%2==0}
print(dict_comp)
print(dict)



import sys
while True:
    print('Type exit to quit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + "'" + response + "'" + '.')

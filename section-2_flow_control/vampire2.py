name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
# This portion will not execute as age > 100 will take precedent
# Check wiki.cyberfront.me for more details
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')

import random


# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes definitely'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
#
#
# # Since we can pass return values as an argument to another function call
# print(getAnswer(random.randint(1, 9)))

'''
Since now we know about list, the above program
can be written more efficiently as a list
'''

message = ['It is certain',
           'It is decidedly so',
           'Yes definitely',
           'Reply hazy try again',
           'Ask again later',
           'Concentrate and ask again',
           'My reply is no',
           'Outlook not so good',
           'Very doubtful'
           ]

# It's alternate of (message[random.randint(0, len(message) - 1)])
print(random.choice(message))

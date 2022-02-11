import random
# help(random)


def getAnswer(user_input):
    r = random.randint(1, 9)
    if user_input == r:
        return 'You have won this round, Play again and earn more'
    else:
        return 'Try again'


user_input = 5
fortune = getAnswer(user_input)
print(fortune)

import random

number_of_streaks = 0

for experiment_number in range(10000):

    # Code that creates a list of 100 'heads' or 'tails' values
    coin_list = ''
    for i in range(100):
        if random.randint(0, 1) == 0:
            coin_list += 'H'  # heads
        else:
            coin_list += 'T'  # tails

    # Code that checks if there is a streak of 6 heads or tails in a row
    if 'HHHHHH' in coin_list or 'TTTTTT' in coin_list:
        number_of_streaks += 1

print('Chance of streak: %s%%' % (number_of_streaks / 100))


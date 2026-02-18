from random import randint, choice

random_number = randint(0,10)
print(f'The random number is {random_number}.')

random_list = []
random_list.append(random_number)
print(f'Our fist Random number on the list is {random_list}')

players = ['Mike', 'Justina', 'Reagan', 'Michel', 'Mary', 'Joseph']
choosed_player = choice(players)
print(f'The lottery machine picked {choosed_player}')
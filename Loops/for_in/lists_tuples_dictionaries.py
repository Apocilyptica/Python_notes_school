# works for tuples and lists
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)

# Dictionary loops
players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis'
}

for position, player in players.items():
    print('Position', position)
    print('Player Name', player)
teams = [
    {
        'astros': {
            '2B': 'Altuve',
            'SS': 'Correa',
            '3B': 'Bregman'
        }
    },
    {
        'angels': {
            'OF': 'Trout',
            'DH': 'Pujols'
        }
    }
]

print(teams)
print(teams[0])

angels = teams[1].get('angels', 'Team not found')

print(angels)
print(list(angels.values())[1])
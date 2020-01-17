players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

print(players.keys())
print(list(players.values())[1])
print(players.items())

# Thread Safe
player_names = list(players.copy().values())

print(players)

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()
print(team_groupings)
print(len(team_groupings))

"""
[
    ('astros', ['Altuve', 'Correa', 'Bregman']),
    ('angels', ['Trout', 'Pujols']),
    ('yankees', ['Judge', 'Stanton']),
    ('red sox', ['Price', 'Betts'])
]
"""
print(list(team_groupings)[1][1][0])

# https://docs.python.org/3.0/library/stdtypes.html#dictionary-view-objects
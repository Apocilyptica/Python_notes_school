teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['astros']
print(teams)

print(teams.get('mets', 'No team found by that name'))

removed_team = teams.pop('astros', 'No team found by that name')

print(teams)
print(removed_team)

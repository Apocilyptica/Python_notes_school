sentence = 'The quick brown fo jumped over the lazy dog'

sentence_two = 'That is my dog\'s bowl'

sentence_three = "That is my dog's bowl"

sentence_four = "Tiffany said, \"That is my dog's bowl\""

sentence = 'The quick brown fox jumped'.upper() # Entire string in uppercase
#or
#print(sentence.upper())

sentence = 'the quick brown fox jumped'.capitalize() # Capitalize the first letter of string

sentence = 'the quick brown fox jumped'.title() # Capitalize every first letter of every word of string

sentence = 'THE QUICK BROWN FOX JUMPED'.lower().title() # Entire string in lowercase + can have multipul calls

starter_sentence = 'The quick brown fox jumped'
#print(starter_sentence[0]) # prints out just the index callout

starter_sentence = 'The quick brown fox jumped'
#first = starter_sentence[0]
#second = starter_sentence[1]
#third = starter_sentence[2]
#new_sentence = first + second + third

first_word = starter_sentence[0:3] # brings back 'The' in range
new_sentence = first_word

# new_sentence = 'Thy' + starter_sentence[3:len(starter_sentence)]
new_sentence = 'Thy' + starter_sentence[3:]

#print(new_sentence)

# Heredoc - multi-line comment, string

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulm id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip() # Takes out the new line characters at beggining and end

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulm id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
"""

#print(repr(content)) # Representation of how the computer interperets at a string

long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulm id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

print(long_string)
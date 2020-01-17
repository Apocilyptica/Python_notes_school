sentence = 'The quick brown fox jumped over the lazy dog'

query = sentence.find('oops') # returns -1 if cant find value
query_two = sentence.index('quick') # error if cant find value

print(query)
print(query_two)

query = 'fox' in sentence
query_two = 'oops' in sentence

if 'oops' in sentence: # best practice
    query_three = 'In sentence'

else:
    query_three = 'Not in sentence'

print(query)
print(query_two)
print(query_three)
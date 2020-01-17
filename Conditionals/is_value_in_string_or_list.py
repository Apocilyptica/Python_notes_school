sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word in sentence:
    print('The word was found in the sentence')
else:
    print('The word was not in the sentence')

if word.lower() in sentence.lower():
    print('The word was found in the sentence')
else:
    print('The word was not in the sentence')

nums = range(1, 5, 2)

if 3 in nums:
    print('The number was found')
else:
    print('The number was not found')
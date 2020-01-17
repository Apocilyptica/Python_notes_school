def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '42':
            print('You correctly guessed it!')
            return False
        else:
            print(f'No, {guess} is not the answer, please try again\n')

guessing_game()
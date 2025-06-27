#Let the computer choose a random number between 1 and 100, and the user has to guess it.
from random import randint

number = randint(1,101)

while True:
    try:
        user = input('Guess a number from 1 to 100 or want to quit enter q: ')
        if user == 'q':
            break
        user = int(user)
        if user == number:
            print('Hurray! your guess is correct')
            break
        elif user < number:
            print('Your guess is low')
        else:
            print('Your guess is high')
        
    except ValueError:
        print(f'Enter numerical value only')
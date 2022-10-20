import prompt
import random


def even_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer_user = prompt.string('Your answer: ')
        if (number % 2 == 0 and answer_user == 'yes') or \
                (number % 2 != 0 and answer_user == 'no'):
            print('Correct!')
            count += 1
    else:
        print(f'Congratulations, {name}!')

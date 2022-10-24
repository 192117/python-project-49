import prompt
import random
import math


def gcd_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        result = math.gcd(number1, number2)
        print(f'Question: {number1} {number2}')
        answer_user = int(prompt.string('Your answer: '))
        if answer_user != result:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            count += 1
    else:
        print(f'Congratulations, {name}!')

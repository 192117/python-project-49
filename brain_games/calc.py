import prompt
import random


def calc_game():
    operators = ['+', '-', "*"]
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = random.choice(operators)
        result = {
            '+': number1+number2,
            '-': number1-number2,
            '*': number1*number2
        }
        print(f'Question: {number1} {operator} {number2}')
        answer_user = int(prompt.string('Your answer: '))
        if answer_user != result.get(operator):
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{result.get(operator)}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            count += 1
    else:
        print(f'Congratulations, {name}!')

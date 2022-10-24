import random
from brain_games.games import questions_answer


def calc_game():
    operators = ['+', '-', "*"]
    name = questions_answer()
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operator = random.choice(operators)
        result = {
            '+': number1 + number2,
            '-': number1 - number2,
            '*': number1 * number2
        }
        answer_user = int(questions_answer([number1, operator, number2]))
        if answer_user != result.get(operator):
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{result.get(operator)}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            count += 1
    else:
        print(f'Congratulations, {name}!')

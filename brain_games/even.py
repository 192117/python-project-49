import random
from brain_games.games import questions_answer


def even_game():
    name = questions_answer()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        answer_user = questions_answer([number])
        if (number % 2 == 0 and answer_user == 'yes') or \
                (number % 2 != 0 and answer_user == 'no'):
            print('Correct!')
            count += 1
        elif (number % 2 == 0 and answer_user == 'no'):
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif (number % 2 != 0 and answer_user == 'yes'):
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

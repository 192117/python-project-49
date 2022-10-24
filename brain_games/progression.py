import random
from brain_games.games import questions_answer


def progression_game():
    name = questions_answer()
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        values = [i for i in range(random.randint(1, 20), random.randint(58, 79), random.randint(1, 8))]
        ind = random.randint(0, len(values))
        answer, values[ind] = values[ind], '..'
        answer_user = int(questions_answer(values))
        if answer_user != answer:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            count += 1
    else:
        print(f'Congratulations, {name}!')

import random
from brain_games.games import questions_answer


def progression_game():
    name = questions_answer()
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        step = random.randint(1, 24)
        values = [random.randint(1, 20)]
        for i in range(0, 10):
            values.append(values[-1] + step)
        ind = random.randint(0, len(values)-1)
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

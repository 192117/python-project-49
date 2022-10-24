import prompt
import random


def progression_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        values = [i for i in range(random.randint(1, 20), random.randint(50, 79), random.randint(1, 11))]
        ind = random.randint(0, len(values))
        answer, values[ind] = values[ind], '..'
        print('Question: ', *values)
        answer_user = int(prompt.string('Your answer: '))
        if answer_user != answer:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            count += 1
    else:
        print(f'Congratulations, {name}!')

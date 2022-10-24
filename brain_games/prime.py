import random
from brain_games.games import questions_answer


def isprime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def prime_game():
    name = questions_answer()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 21)
        answer_user = questions_answer([number])
        if (isprime(number) is True and answer_user == 'yes') or \
                (isprime(number) is False and answer_user == 'no'):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{'yes' if isprime(number) else 'no'}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

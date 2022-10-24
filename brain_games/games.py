import prompt


def questions_answer(values=None):
    if values is None:
        name = prompt.string('May I have your name? ')
        print(f'Hello, {name}!')
        return name
    else:
        print('Question:', *values)
        answer_user = prompt.string('Your answer: ')
        return answer_user

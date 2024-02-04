from random import randint

guess_number = randint(1, 100)
check = False


def guess_number_game(guess_number, user_number):

    if guess_number > user_number:
        return 'Ваше число меньше того, что загадано'
    elif guess_number < user_number:
        return 'Ваше число больше того, что загадано'
    else:
        return 'Отличная интуиция! Вы угадали число :).'


# Прогон через цикл while
while not check:
    print(guess_number_game(guess_number, int(input())))

from random import randint

guess_number = randint(1,100)
check = False

def guess_number_game(guess_number, user_number, check):
     
    if guess_number > user_number:
        return 'Ваше число меньше того, что загадано'
    elif guess_number < user_number:
        return 'Ваше число больше того, что загадано'
    else:
        check = True
        return 'Отличная интуиция! Вы угадали число :).'





while not check:
    print(guess_number_game(guess_number, int(input()), check)) 


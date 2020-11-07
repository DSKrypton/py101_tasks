"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
from random import randint
MIN_VALUE = 0
MAX_VALUE = 1000000


def manual_binary_search_trainer():
    value_to_guess = randint(MIN_VALUE, MAX_VALUE)
    print(f'Greetings, The Number from {MIN_VALUE} to {MAX_VALUE} range has been chosen, type your guesses.')
    next_line = input('Next guess:')
    while next_line not in ('stop', 'end', 'exit'):
        try:
            next_value = int(next_line)
        except ValueError:
            print(f'Something went wrong.{next_line} is not a number')
            continue
        if next_value in range(MIN_VALUE, MAX_VALUE):
            if next_value > value_to_guess:
                print(f'{next_value} is greater than The Number')
            elif next_value < value_to_guess:
                print(f'{next_value} is lesser than The Number')
            else:
                print('Congratulations! You guessed The Number')
                exit(0)
        else:
            print(f'{next_value} is outside of guessing range. It\'s between {MIN_VALUE} and {MAX_VALUE}')
        next_line = input('Next guess:')




if __name__ == '__main__':
    manual_binary_search_trainer()

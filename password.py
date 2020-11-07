"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""
import re


def password_evaluation(password):
    complexity = 0
    if re.search('[A-Z]', password):
        complexity += 1
    if re.search('[a-z]', password):
        complexity += 1
    if re.search('[0-9]', password):
        complexity += 1
    if len(password) > 7:
        complexity += 10

    print('Your password is {}'.format('complex' if complexity == 13 else 'mediocre' if complexity == 12 else 'weak'))


if __name__ == '__main__':
    password_evaluation(input('Write your password:'))

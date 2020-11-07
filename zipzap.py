"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""


def zipzapzup(x):
    [print(f'{i}: zip-zap-zup') if i % 105 == 0 else
     print(f'{i}: zap-zup') if i % 35 == 0 else
     print(f'{i}: zip-zup') if i % 21 == 0 else
     print(f'{i}: zip-zap') if i % 15 == 0 else
     print(f'{i}: zup') if i % 7 == 0 else
     print(f'{i}: zap') if i % 5 == 0 else
     print(f'{i}: zip') if i % 3 == 0 else
     print(i) for i in range(1, x+1)
     ]


if __name__ == '__main__':
    for i in range(1, 101):
        if i % 15 == 0:
            print('zip-zap')
        elif i % 5 == 0:
            print('zap')
        elif i % 3 == 0:
            print('zip')
        else:
            print(i)

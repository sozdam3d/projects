"""Создать скрипт, который будет в input() принимать строки,
и их необходимо будет конвертировать в числа, добавить try-except на то, чтобы строки могли быть сконвертированы в числа.
В случае удачного выполнения скрипта написать: «Вы ввели <введённое число>».
В конце скрипта обязательно написать: «Выход из программы»."""
try:
    a=(input('Вводи число:'))
    a=int(a)
except ValueError as e:
    print(f'Ошибочка вышла вот такая:\n', e)
else:
    print(f'Вы ввели {a}')
finally:
    print('Выход из программы')
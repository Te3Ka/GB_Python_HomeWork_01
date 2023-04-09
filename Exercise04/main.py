#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
Требуется определить, можно ли от шоколадки размером n * m долек
отломить k долек, если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника)
'''

# Функция вывода автора программы.
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

# Проверка правильности введённого числа.
def correct_number(str):
    _number = int(input(f"Введите {str}: "))
    while (_number < 0):
        _number = int(input("Введено неверное число! Введите заново: "))
    return _number

# Проверка на перелом шоколадки по количеству долек.
def breacking_chocolate(_length_chocolate, _width_chocolate, _number_slices):
    if (_number_slices % _length_chocolate == 0) or (_number_slices % _width_chocolate == 0) and (_number_slices <= _width_chocolate * _length_chocolate): 
        return bool(True)
    else:
        return bool(False)

print("Программа проверяет, можно ли за один разлом шоколадки отломить указанное количество долек.")
_n = correct_number("длину шоколадки в дольках")
_m = correct_number("ширину шоколадки в дольках")
_k = correct_number("сколько долек нужно отломить")
_res = breacking_chocolate(_n, _m, _k)
print(f"От шоколадки размером {_n}*{_m} {'можно' if _res else 'нельзя'} отломить {_k} кусочков")

author()
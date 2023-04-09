#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
Написать программу, которая проверяет, является ли билет счастливым.
Счастливый билет - это тот билет, у которого имеется шестизначный номер,
с условием, что сумма первых трёх чисел равна сумме последних трёх чисел.
'''

# Функция вывода автора программы
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

# Проверка на правильность введённого числа.
def correct_number():
    _number = int(input("Введите номер билета: "))
    while (_number < 1000) or (_number > 999999):
        _number = int(input("Введено неверное число! Введите заново: "))
    return _number

# Сложение цифр
def sum_digits(_number):
    sum = 0
    while (_number > 0):
        sum += _number % 10
        _number //= 10
    return sum

# Проверка на счастливый билет.
def lucky_ticket(_num):
    _num_first = _num // 1000
    _num_second =  _num % 1000
    _sum_first = sum_digits(_num_first)
    _sum_second = sum_digits(_num_second)
    if (_sum_first == _sum_second):
        return bool(True)
    else:
        return bool(False)

print("Программа проверяет, является ли введённый номер билета (шестизначный) счастливым.")
_number_ticket = correct_number()
_lucky = lucky_ticket(_number_ticket)
print(f"Билет с номером {_number_ticket} {'' if _lucky else 'не'}счастливый.")

author()
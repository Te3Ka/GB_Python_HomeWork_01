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

print("Программа проверяет, является ли введённый номер билета (шестизначный) счастливым.")
_number_ticket = correct_number()

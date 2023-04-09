#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
Найти сумму цифр трёхзначного числа
'''
# Функция вывода автора программы
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

# Проверка на введение трёхзначного числа.
def correct_number():
    _number = int(input("Введите трёхзначное число: "))
    if (_number < 0):
        _number = _number * (-1)
    while (_number < 100) or (_number > 999):
        _number = int(input("Введено неверное число! Введите заново: "))
    return _number

# Сложение цифр числа.
def sum_digits(number):
    sum = 0
    while (number > 0):
        sum += number % 10
        number //= 10
    return sum

print("Программа считает сумму цифр трёхзначного числа.")
_num = correct_number()
_sum_dig = sum_digits(_num)
print(f"Сумма цифр числа {_num} = {_sum_dig}")

author()
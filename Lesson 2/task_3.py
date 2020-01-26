# Написать функцию вычисления факториала числа

n = int(input('Введите число: '))
factorial = 1
for i in range(2, n+1):
    factorial *= i
print('Факториал числа ', n, ' : ', factorial)
input('Нажмите Enter для продолжения...')

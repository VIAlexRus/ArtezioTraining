# 2. Написать функцию, которая принимает 3 числа (a,b,c)
# и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’


def splitter(a, b, c):
    list1 = []
    for x in range(a, b):
        if x % c == 0:
            list1.append(x)
    return list1


a, b, c = map(int, input('Введите числa a, b, c через пробел: ').split())
print('Числа, делющиеся на ', c, ' : ', splitter(a, b, c))
input('Нажмите Enter для продолжения...')

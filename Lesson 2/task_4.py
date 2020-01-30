# Написать свою имплементацию функции range() из Python 2.x
# (аналогично Python 3, только возвращает список).


def my_range(a, b, c):
    list1 = [a]
    while True:
        if a + c < b:
            a += c
            list1.append(a)
        else:
            break
    return list1


a = int(input('Введите начало списка: '))
b = int(input('Введите конец списка: '))
c = int(input('Введите шаг между числами: '))
print('Список между числами', a, 'и', b, ' : ', my_range(a, b, c))
input('Нажмите Enter для продолжения...')

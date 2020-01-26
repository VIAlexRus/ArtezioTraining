# Написать свою имплементацию функции range() из Python 2.x
# (аналогично Python 3, только возвращает список).


def my_range(a, b):
    list1 = [a]
    while True:
        if a < b:
            a += 1
            list1.append(a)
        else:
            break
    return list1


a = ('Введите первое число: ')
b = ('Введите второе число: ')
print('Список между числами', a, 'и', b, ' : ', my_range(a, b))
input('Нажмите Enter для продолжения...')

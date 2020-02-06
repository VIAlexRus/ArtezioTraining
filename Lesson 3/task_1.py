# Написать несколько функций, которые в качестве единственного
# аргумента принимают список (или кортеж) целых чисел.
# - первая функция должна вернуть квадраты элементов коллекции;
# - вторая функция должна вернуть только элементы на четных позициях;
# - третья функция возвращает кубы четных элементов на нечетных позициях.


def square(x):
    # квадраты элементов коллекции
    key = 0
    results = []
    for n in x:
        key += 1
        results.append(n * n)
    return results


def even(x):
    # только элементы на четных позициях
    results = []
    for n in range(1, len(x), 2):
        results.append(x[n])
    return results


def square_odd(x):
    # кубы четных элементов на нечетных позициях
    results = []
    for n in range(0, len(x), 2):
        if x[n] % 2 == 0 and x[n] != 0:
            results.append(x[n] * x[n] * x[n])
    return results


list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [21, 31, 523, 634, 784, 234, 125, 363, 324]
list_3 = [5, 6, 2, 7, 8, 1, 5, 3, 9, 1, 6, 8, 4, 6, 8]

print(square(list_1))
print(even(list_1))
print(square_odd(list_1))

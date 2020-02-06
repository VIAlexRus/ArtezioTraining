# Написать функцию, которая будет принимать только 4
# позиционных аргументы (все аргументы числовые).
# Функция должна вернуть среднее арифметическое аргументов и
# самый большой аргумент за все время вызовов этой функции.


def summ(a, b, c, d):
    global maxArg
    list1 = [a, b, c, d]
    s = sum(list1)
    soArith = s/4
    if max(list1) > maxArg:
        maxArg = max(list1)
    return soArith, maxArg


maxArg = 0

print(summ(2, 3, 6, 8))
print(summ(10, -8, 105, -44))
print(summ(52, 53, 36, 28))

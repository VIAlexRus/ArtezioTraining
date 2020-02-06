# Написать функцию, которая принимает произвольное количество любых аргументов
# Аргументами могут быть вложенные списки и кортежи, содержащие числа
# и другие списки и кортежи. Пример вызова функции:
# foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
# Функция должна вернуть произведение
# и сумму всех ненулевых элементов вложенных чисел.
# Возможны циклические ссылки в аргументах.
# Пример такого аргумента: a = [1, 2, 3]; a.append(a)
# При обнаружении циклической ссылки нужно сообщить пользователю и
# вернуть None.


def summ(*args, **kwargs):

    def listSumm(lists):
        results_summ = 0
        results_work = 1
        lists = list(lists)
        for i in lists:
            if type(i) == int:
                results_summ += i
                if i != 0:
                    results_work = results_work * i
            else:
                lists.extend(i)
        return results_summ, results_work

    list_kw = kwargs.values()
    res_kw = listSumm(list_kw)
    list_ar = list(args)
    res_ar = listSumm(list_ar)
    results_summ = res_kw[0] + res_ar[0]
    results_work = res_kw[1] * res_ar[1]

    return results_summ, results_work


a = summ(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
print('Сумма всех чисел =', a[0])
print('Произведение всех чисел =', a[1])

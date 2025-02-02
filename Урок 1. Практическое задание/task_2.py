"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

lst_obj = []


def sort_1(lst_obj):  # сложность этого алгоритма O(n)
    res = lst_obj[1]  # O(1)
    for el in lst_obj:  # O(n)
        if res > el:  # O(1)
            res = el  # O(1)
    return res  # O(1)


def sort_2(lst_obj):  # сложность этого алгоритма O(n**2)
    for el in lst_obj:  # O(n)
        is_min = True  # O(1)
        for i in lst_obj:  # O(n)
            if i < el:  # O(1)
                is_min = False  # O(1)
        if is_min:  # O(1)
            return el  # O(1)

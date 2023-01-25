"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import time


def time_dec(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполнения функции {func.__name__} равно {end - start} секунд.')
        return result

    return timer


@time_dec
def list_add(lst, n):
    for i in range(n):
        lst.append(i)  # O(1)


le_list = []
list_add(le_list, 10000)


@time_dec
def dict_add(dct, n):
    for i in range(n):
        dct[i] = i  # O(1)


le_dict = {}
dict_add(le_dict, 10000)


@time_dec
def list_get(lst, n):
    if n < len(lst):
        print(lst[n])  # O(1)
    else:
        print(f'Элемента с номером {n} нет в списке.')


list_get(le_list, 1345)
list_get(le_list, 1875)
list_get(le_list, 100001)


@time_dec
def dict_get(dct, n):
    if n < len(dct):
        print(dct[n])  # O(1)
    else:
        print(f'Элемента с номером {n} нет в словаре.')


dict_get(le_dict, 1345)
dict_get(le_dict, 1875)
dict_get(le_dict, 100001)


@time_dec
def list_rem(lst, n):
    if n < len(lst):
        print(lst.pop(n))  # O(1)
    else:
        print(f'Элемента с номером {n} нет в списке.')


list_rem(le_list, 16)
list_rem(le_list, 61)
list_rem(le_list, 100001)
list_get(le_list, 1345)


@time_dec
def dict_rem(dct, n):
    if n < len(dct):
        print(dct.pop(n))  # O(1)
    else:
        print(f'Элемента с номером {n} нет в словаре.')


dict_rem(le_dict, 16)
dict_rem(le_dict, 61)
dict_rem(le_dict, 100001)
dict_get(le_dict, 1345)
"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
import math
import random
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
def shell_sort(array: list) -> list:
    """shell sorting method"""
    array_len = len(array)
    k = int(math.log2(array_len))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, array_len):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return array

m = 10000
RANDOM_LIST = [random.randint(0, 1000) for _ in range(2 * m + 1)]

print(RANDOM_LIST)

SORTED_LIST = shell_sort(RANDOM_LIST)
print(SORTED_LIST)
print(SORTED_LIST[m])
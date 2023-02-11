"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

import random
from statistics import median


m = 10
RANDOM_LIST = [random.randint(0, 1000) for _ in range(2 * m + 1)]
print(RANDOM_LIST)
print(median(RANDOM_LIST))

def le_median(RANDOM_LIST):
    return median(RANDOM_LIST)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("le_median", setup="from __main__ import le_median"))
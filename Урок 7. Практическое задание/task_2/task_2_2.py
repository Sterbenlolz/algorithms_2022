"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

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
def median_search(array: list) -> int:
    lower_count = 0
    upper_count = 0
    equal_count = 0
    for el_out in array:
        for el_in in array:
            if el_in > el_out:
                upper_count += 1
            elif el_in < el_out:
                lower_count += 1
            else:
                equal_count += 1
        if lower_count == upper_count or (lower_count - upper_count) ** 2 <= equal_count ** 2:
            return el_out
        lower_count = 0
        upper_count = 0
        equal_count = 0

m = 10
RANDOM_LIST = [random.randint(0, 1000) for _ in range(2 * m + 1)]
print(RANDOM_LIST)
#RANDOM_LIST.sort()
#print(RANDOM_LIST)
print(median_search(RANDOM_LIST))

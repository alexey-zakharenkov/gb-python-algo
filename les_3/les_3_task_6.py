"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и
максимальным элементами. Сами минимальный и максимальный элементы в сумму
не включать.
"""

import random

LOWER_BOUND = -10
UPPER_BOUND = 10
SIZE = 10

a = [random.randint(LOWER_BOUND, UPPER_BOUND) for _ in range(SIZE)]
print(a)

min_el, min_idx = None, None
max_el, max_idx = None, None

for i, el in enumerate(a):
    if min_el is None or el < min_el:
        min_el, min_idx = el, i
    if max_el is None or el > max_el:
        max_el, max_idx = el, i

left_idx = min_idx if min_idx < max_idx else max_idx
right_idx = min_idx if min_idx > max_idx else max_idx

summ = 0
for i in range(left_idx + 1, right_idx):
    summ += a[i]

print(f"Между позициями {min_idx} и {max_idx} мин. и макс. элементов "
      f"сумма элементов равна {summ}")

"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
так и различаться.
"""

import random

LOWER_BOUND = -100
UPPER_BOUND = 100
SIZE = 20

a = [random.randint(LOWER_BOUND, UPPER_BOUND) for _ in range(SIZE)]
print(a)

min1, min2 = UPPER_BOUND + 1, UPPER_BOUND + 1
min1_idx, min2_idx = None, None

for i, el in enumerate(a):
    if el < min1:
        min2, min2_idx = min1, min1_idx
        min1, min1_idx = el, i
    elif el < min2:
        min2, min2_idx = el, i

print(f"Первый минимум = {min1} в позиции {min1_idx}")
print(f"Второй минимум = {min2} в позиции {min2_idx}")

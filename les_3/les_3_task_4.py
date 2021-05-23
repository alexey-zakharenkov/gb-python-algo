"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

LOWER_BOUND = -10
UPPER_BOUND = 10
SIZE = 20

a = [random.randint(LOWER_BOUND, UPPER_BOUND) for _ in range(SIZE)]
print(a)

# Решение без словаря.
# В список numbers записываются уникальные числа,
# в соответствующие ячейки frequencies - количество их появлений
numbers = []
frequencies = []

for el in a:
    for i in range(len(numbers)):
        if numbers[i] == el:
            frequencies[i] += 1
            break
    else:
        numbers.append(el)
        frequencies.append(1)

max_freq_idx = -1
for i in range(len(frequencies)):
    if max_freq_idx == -1 or frequencies[i] > frequencies[max_freq_idx]:
        max_freq_idx = i

if frequencies[max_freq_idx] == 1:
    print("Все элементы уникальны")
else:
    print(f"Самый частый элемент = {numbers[max_freq_idx]} "
          f"встретился {frequencies[max_freq_idx]} раз")

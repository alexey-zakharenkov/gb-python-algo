"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.


Задача для исследования: Определить, какое число в массиве встречается чаще всего.
"""

import random

LOWER_BOUND = -10000
UPPER_BOUND = 10000
MAX_SIZE = 10**6

a = [random.randint(LOWER_BOUND, UPPER_BOUND) for _ in range(MAX_SIZE)]
#print(a)


def find_most_frequent_number1(arr):
    """Решение с массивом уникальных чисел и массивом частот.
    Проходим по массиву arr, вновь встречающиеся числа добавляем
    в специальный массив и увеличиваем частоту в отдельном массиве
    для частот. Потом за линейное время находим максимальную частоту."""

    numbers = []
    frequencies = []

    for el in arr:
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

    return numbers[max_freq_idx], frequencies[max_freq_idx]


def find_most_frequent_number2(arr):
    """Поддержание массива пар (число, частота)
    в отсортированном по частоте порядке. В конце алгоритма
    самое частое число будет в начале такого массива.
    """

    num_freq = []  # список пар (число, частота)

    for el in arr:
        for i, (num, freq) in enumerate(num_freq):
            if el == num:
                num_freq[i] = (num, freq + 1)
                # Увеличили частоту на 1 и опускаем элемент,
                # чтобы элементы были упорядочены в обратном порядке по частоте
                while i > 0 and num_freq[i][1] > num_freq[i - 1][1]:
                    num_freq[i], num_freq[i - 1] = num_freq[i - 1], num_freq[i]
                    i -= 1
                break
        else:
            num_freq.append((el, 1))

    return num_freq[0]


def find_most_frequent_number3(arr):
    """Решение со словарём частот"""

    frequencies = {}  # number => frequency

    for el in arr:
        if el in frequencies:
            frequencies[el] += 1
        else:
            frequencies[el] = 1

    max_freq = -1
    best_number = None
    for el, freq in frequencies.items():
        if max_freq == -1 or freq > max_freq:
            max_freq = freq
            best_number = el

    return best_number, max_freq


import timeit

if __name__ == "__main__":
    for f in (find_most_frequent_number1,
              find_most_frequent_number2,
              find_most_frequent_number3):
        for n in (100, 500, 1000, 2500, 5000, 10000):
            assert MAX_SIZE >= n
            arr = a[:n]
            print(f, n, timeit.timeit("f(arr)", number=10, globals=globals()))

"""
К решению прилагается картинка с цифрами и графиками - max_frequency_in_array.png.

Видно, что первые два решения ведут себя квадратично,
причём попытка поддерживать отсортированный массив частот обходится
ещё дороже.
Решение со словарём наиболее эффективное,
его сложность линейно зависит от количества элементов.
"""
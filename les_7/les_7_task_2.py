"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
отсортированный массивы.
"""

import random


def merge_sort(a):
    if len(a) <= 1:
        return

    middle = len(a) // 2
    x = a[:middle]
    y = a[middle:]

    # Сортировка половин
    merge_sort(x)
    merge_sort(y)

    # Собственно, слияние. Приёмник - опять массив a.
    i_x = 0
    i_y = 0
    i_a = 0
    while i_x < len(x) and i_y < len(y):
        if x[i_x] <= y[i_y]:  # стабильность сортировки слиянием обеспечивается знаком "<=" здесь
            a[i_a] = x[i_x]
            i_x += 1
        else:
            a[i_a] = y[i_y]
            i_y += 1
        i_a += 1

    while i_x < len(x):
        a[i_a] = x[i_x]
        i_x += 1
        i_a += 1

    while i_y < len(y):
        a[i_a] = y[i_y]
        i_y += 1
        i_a += 1


if __name__ == "__main__":

    LOWER_BOUND = 0
    UPPER_BOUND = 50
    SIZE = 11
    # random.random() генерирует псевдослучайное число в диапазоне [0.0, 1.0)
    # Формула (x * (b - a) + a) отображает этот интервал в интервал [a, b)
    a = [round(random.random() * (UPPER_BOUND - LOWER_BOUND) + LOWER_BOUND, 2) for _ in range(SIZE)]

    print("Исходный массив:\n", a, sep='')
    merge_sort(a)
    print("Отсортированный массив:\n", a, sep='')

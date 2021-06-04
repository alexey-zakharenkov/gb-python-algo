"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если
это слишком сложно, используйте метод сортировки, который не рассматривался
на уроках (сортировка слиянием также недопустима).

Примечание автора практического задания.
Реализован алгоритм Блума-Флойда-Пратта-Ривеста-Тарьяна, который ищет медиану за O(n)
в худшем случае.
Идея и бОльшая доля кода взяты из статьи https://habr.com/ru/post/346930/
"""

import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1


def find_median_simple(arr):
    arr_copy = arr.copy()
    insertion_sort(arr_copy)
    return arr_copy[len(arr_copy) // 2]


def find_median(arr, pivot_fn=random.choice):
    """Используем следующее определение медианы:
    при нечётной длине массива берём центральный элемент,
    иначе левый из двух "центральных".
    """
    return find_Kth_statistics(arr, len(arr) // 2, pivot_fn)


def find_Kth_statistics(arr, k, pivot_fn):
    """
    Находит k-тую порядковую статистику в списке arr (индексы начинаются с 0)
    :param arr: список данных, для которых определена операция сравнения
    :param k: индекс
    :param pivot_fn: функция выбора pivot
    :return: k-я порядковая статистика в списке arr
    """

    # Терминальное условие рекурсии
    if len(arr) == 1:
        assert k == 0
        return arr[0]

    # Нахождение опорного элемента
    pivot = pivot_fn(arr)

    # Делим элементы на меньшие, бОльшие и равные опорному. O(n)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        # Задача сводится к поиску k-й порядковой статистики в левой половине
        return find_Kth_statistics(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        # Задача сводится к поиску k-й порядковой статистики в правой половине
        return find_Kth_statistics(highs, k - len(lows) - len(pivots), pivot_fn)


def pick_pivot(arr):
    """
    Выбираем хороший pivot в списке чисел arr.
    Этот алгоритм выполняется за время O(n).
    """
    assert len(arr) > 0

    # Если элементов < 5, просто возвращаем медиану
    if len(arr) < 5:
        # В этом случае мы обращаемся к простой простой функции медианы.
        # Поскольку мы выполняем её только для списка из пяти или менее элементов, она не 
        # зависит от длины входных данных и может считаться постоянным временем.
        return find_median_simple(arr)

    # Сначала разделим arr на группы по 5 элементов. O(n)
    chunks = chunked(arr, 5)

    # Для простоты мы можем отбросить все группы, которые не являются полными. O(n)
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]

    # Затем мы сортируем каждый фрагмент. Каждая группа имеет фиксированную длину,
    # поэтому каждая сортировка занимает постоянное время. Поскольку у нас
    # есть n/5 фрагментов, эта операция тоже O(n).
    sorted_groups = [sorted(chunk) for chunk in full_chunks]

    # Медиана каждого фрагмента имеет индекс 2
    medians = [chunk[2] for chunk in sorted_groups]

    # Мы находим медиану списка длиной n/5, поэтому эта операция также O(n).
    # Мы передаём нашу текущую функцию pick_pivot в качестве создателя pivot
    # алгоритму find_median. O(n)
    median_of_medians = find_median(medians, pick_pivot)
    return median_of_medians


def chunked(arr, chunk_size):
    """Разделяет список arr на фрагменты размером chunk_size."""
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]


if __name__ == "__main__":
    LOWER_BOUND = 0
    UPPER_BOUND = 9
    SIZE = 11
    a = [random.randint(LOWER_BOUND, UPPER_BOUND) for _ in range(SIZE)]
    print(a)

    print(f"Медиана = {find_median(a, pick_pivot)}")

    insertion_sort(a)  # Используется только для контроля правильности ответа
    print(f"Контроль правильности. Медиана через сортировку = {a[len(a)//2]}")
    print(a)

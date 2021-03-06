"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и
определить программы с наиболее эффективным использованием памяти.

Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать по памяти
(укажите какую задачу вы взяли в комментарии);
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки)
вставить в виде комментариев в файл с кодом. Не забудьте указать версию и
разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.


Задача для исследования: Определить, какое число в массиве встречается чаще всего.
"""

import platform
import random
import sys

from memory_summator import MemorySummator


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

    print(MemorySummator(
        numbers, frequencies,  # контейнеры
        el, i,  #  итерационные переменные
        max_freq_idx  # вспомогательные переменные
    ))
    # Но также работает такой способ: локальные переменные за вычетом параметра функции
    #print(MemorySummator(set(locals()) - set(['arr'])))

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

    print(MemorySummator(
        num_freq,  # контейнеры
        el, num, freq, i,  # итерационные переменные
    ))
    # Но также работает такой способ: локальные переменные за вычетом параметра функции
    #print(MemorySummator(set(locals()) - set(['arr'])))

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

    print(MemorySummator(
        frequencies,  # контейнеры
        el, freq,  # итерационные переменные
        max_freq, best_number  # вспомогательные переменные
    ))
    # Но также работает такой способ: локальные переменные за вычетом параметра функции
    #print(MemorySummator(set(locals()) - set(['arr'])))

    return best_number, max_freq


if __name__ == "__main__":
    # Параметры ОС и интерпретатора Python
    print(f"Операционная система: {platform.platform()}")
    print(f"Процессор: {platform.processor()}")
    print(f"Интерпретатор Python: {platform.python_implementation()} {sys.version}")
    print()

    # Генерация массива для экспериментов
    LOWER_BOUND = -10000
    UPPER_BOUND = 10000
    SIZE = 10 ** 3
    a = [random.randint(LOWER_BOUND, UPPER_BOUND) for _ in range(SIZE)]

    # Запуск экспериментов
    for f in (find_most_frequent_number1,
              find_most_frequent_number2,
              find_most_frequent_number3):
        print(f"При выполнении функции {f.__name__}() расход памяти такой: ")
        f(a)
        print('*' * 70)

"""
Вывод программы: 

Операционная система: Linux-5.4.0-73-generic-x86_64-with-glibc2.29
Процессор: x86_64
Интерпретатор Python: CPython 3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0]

При выполнении функции find_most_frequent_number1() расход памяти такой: 
Переменные заняли в сумме 70692 байта
Объекты класса <class 'list'> в количестве 2 заняли 15952 байта
Объекты класса <class 'int'> в количестве 1955 заняли 54740 байт
**********************************************************************
При выполнении функции find_most_frequent_number2() расход памяти такой: 
Переменные заняли в сумме 117400 байт
Объекты класса <class 'list'> в количестве 1 заняли 7976 байт
Объекты класса <class 'tuple'> в количестве 976 заняли 54656 байт
Объекты класса <class 'int'> в количестве 1956 заняли 54768 байт
**********************************************************************
При выполнении функции find_most_frequent_number3() расход памяти такой: 
Переменные заняли в сумме 91728 байт
Объекты класса <class 'dict'> в количестве 1 заняли 36960 байт
Объекты класса <class 'int'> в количестве 1956 заняли 54768 байт
**********************************************************************


Выводы:
Сравнение 1-й и 3-й функции показывает, что словарь из N пар "ключ-значение"
типа int по памяти где-то на 30% затратней, чем если ключи и значения хранить
в двух списках.

Сравнение 1-й и 2-й функции показывает, что с точки зрения памяти лучше иметь
2 списка, чем список пар. Получается, что список пар целых чисел
[(a1, b1), (a2, b2), ..., (aN, bN)]
по памяти на 60% затратней, чем два списка
[a1, a2, ..., aN] и [b1, b2, ..., bN].
Оно и понятно, ведь в первом случае у нас получается ещё N переменных типа tuple.

Конечно, цифры 30% и 60% были бы другими, если бы мы выбрали диапазон целых чисел
не [-10000, 10000], а шире или, наоборот, уже, так как размер переменной int
зависит от её величины.

Самое эффективное по памяти решение - 1-е, с использованием только списков. 

Глобальный вывод: списки list - самый экономный способ хранения данных (если не
рассматривать Си-подобные массивы array.array),
а использование дополнительных коллекций для удобства, как то tuple для компановки 
переменных, dict для быстрого доступа по ключу - влечёт накладные расходы на память.
"""

"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

def print_matrix(m):
    for r in m:
        for el in r:
            print(f"{el:5}", ' ', sep='', end='')
        print()

LOWER_BOUND = -10
UPPER_BOUND = 10
ROWS = 5
COLS = 5

matrix = [
    [
        random.randint(LOWER_BOUND, UPPER_BOUND)
        for _ in range(COLS)
    ] for _ in range(ROWS)
]
print_matrix(matrix)

column_mins = [None]*len(matrix[0])

for column in range(len(matrix[0])):
    min_el = matrix[0][column]
    for row in range(1, len(matrix)):
        if matrix[row][column] < min_el:
            min_el = matrix[row][column]
    column_mins[column] = min_el

max_among_column_mins = column_mins[0]
for i in range(1, len(column_mins)):
    if column_mins[i] > max_among_column_mins:
        max_among_column_mins = column_mins[i]

print("Максимальный элемент среди минимальных элементов столбцов = "
      f"{max_among_column_mins}")

"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки. В конце следует вывести полученную
матрицу.
"""

ROWS = 5
COLS = 4

matrix = [[None]*COLS for _ in range(ROWS)]

print(f"Введите элементы матрицы {len(matrix)}x{len(matrix[0])-1}, по одному в строке:")

for r in range(len(matrix)):
    for c in range(len(matrix[0]) - 1):
        matrix[r][c] = int(input())

for row in matrix:
    row_sum = 0
    for c in range(len(row)-1):
        row_sum += row[c]
    row[-1] = row_sum

for row in matrix:
    for el in row:
        print(f"{el:5}", ' ', sep='', end='')
    print()

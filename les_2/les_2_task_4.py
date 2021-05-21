"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

https://drive.google.com/file/d/1jVBNhsx3L_-TBk9KqaIMToVlnH4eJf3P
"""

num = int(input("Введите натуральное число n:"))

summ = 0
next = 1

for i in range(n+1):
    summ += next
    next /= -2

print(f"Сумма первых n членов = {summ}")
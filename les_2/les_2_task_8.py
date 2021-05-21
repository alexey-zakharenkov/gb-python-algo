"""
Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра,
которую необходимо посчитать, задаются вводом с клавиатуры.

https://drive.google.com/file/d/1jVBNhsx3L_-TBk9KqaIMToVlnH4eJf3P
"""

numbers = int(input("Введите количество чисел: "))
digit = int(input("Введите цифру: "))

digit_cnt = 0

for i in range(numbers):
    num = int(input("Введите натуральное число: "))
    while num > 0:
        if num % 10 == digit:
            digit_cnt += 1
        num //= 10

print(f"Цифра встретилась {digit_cnt} раз")
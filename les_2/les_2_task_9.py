"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

https://drive.google.com/file/d/1jVBNhsx3L_-TBk9KqaIMToVlnH4eJf3P
"""

numbers = int(input("Введите количество чисел: "))

max_sum = -1
best_number = -1

for i in range(numbers):
    num = int(input("Введите натуральное число: "))
    digit_sum = 0
    save_num = num

    while num > 0:
        digit_sum += num % 10
        num //= 10

    if max_sum == -1 or digit_sum > max_sum:
        max_sum = digit_sum
        best_number = save_num

print(f"Максимальная сумма цифр = {max_sum} была в числе {best_number}")
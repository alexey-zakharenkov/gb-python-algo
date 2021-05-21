"""
 Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
 и 2 нечетные (3 и 5).

https://drive.google.com/file/d/1jVBNhsx3L_-TBk9KqaIMToVlnH4eJf3P
"""

num = int(input("Введите натуральное число: "))

odd, even = 0, 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    num //= 10

print(f"Чётных цифр {even}, нечётных цифр {odd}")
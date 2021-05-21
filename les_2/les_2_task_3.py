"""
Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, надо вывести 6843.

https://drive.google.com/file/d/1jVBNhsx3L_-TBk9KqaIMToVlnH4eJf3P
"""

n = int(input("Введите натуральное число: "))

reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n //= 10

print(f"Перевёрнутое число = {reversed_n}")


# Рекурсивное решение
def reverse_number(num):
    num_len = 0
    n = num
    while True:
        num_len += 1
        n //= 10
        if n == 0:
            break

    # Покороче: num_len = len(str(num))

    if num_len == 1:
        return num

    last_digit = num % 10
    return last_digit * (10 ** (num_len-1)) + reverse_number(num // 10)
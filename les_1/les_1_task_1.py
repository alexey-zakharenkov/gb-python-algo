"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

https://app.diagrams.net/#G1FHgjTe-_tNOLtWPGYvXT0sW377_hb3tz
"""

num = int(input("Введите целое трёхзначное число:"))

summ = 0
prod = 1

digit = num % 10
summ += digit
prod *= digit
num //= 10

digit = num % 10
summ += digit
prod *= digit
num //= 10


digit = num
summ += digit
prod *= digit

print(f"Сумма цифр = {summ}, произведение цифр = {prod}")
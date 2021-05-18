"""
Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

https://app.diagrams.net/#G1FHgjTe-_tNOLtWPGYvXT0sW377_hb3tz
"""

print("Введите три разных числа: ")
a = float(input("первое число = "))
b = float(input("второе число = "))
c = float(input("третье число = "))

if b < a < c or c < a < b:
    m = a
elif a < b < c or c < b < a:
    m = b
else:
    m = c

print(f"Среднее = {m}")
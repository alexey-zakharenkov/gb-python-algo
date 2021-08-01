"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.

https://app.diagrams.net/#G1FHgjTe-_tNOLtWPGYvXT0sW377_hb3tz
"""

y = int(input("Введите год: "))

if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("високосный")
else:
    print("не високосный")
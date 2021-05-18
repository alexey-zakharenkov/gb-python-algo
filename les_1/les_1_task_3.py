"""
По введенным пользователем координатам двух точек вывести уравнение прямой
вида y = kx + b, проходящей через эти точки.

https://app.diagrams.net/#G1FHgjTe-_tNOLtWPGYvXT0sW377_hb3tz
"""

print("Введите координаты первой точки:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Введите координаты второй точки, отличной от первой:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

if x1 == x2:
    print(f"x = {x1:.3f}")
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print(f"y = {k:.3f} * x + {b:.3f}")

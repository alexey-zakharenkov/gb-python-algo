"""
Написать программу сложения и умножения двух положительных целых
шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл
A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


BASE = 16
value2digit = dict(enumerate('0123456789ABCDEF'))
digit2value = {v: k for k, v in value2digit.items()}


def long_hex_sum(a, b):
    """Сумма двух чисел, записанных в деке в виде ['A', '2']"""

    # Сумма может оказаться длинней на 1 цифру самого длинного из слагаемых.
    # Дополним числа незначащими нулями до этой длины
    max_len = len(a) if len(a) > len(b) else len(b)
    n = a.copy()
    n.extendleft(['0'] * (max_len + 1 - len(a)))
    m = b.copy()
    m.extendleft(['0'] * (max_len + 1 - len(b)))
    s = deque(['0'] * (max_len + 1))

    # Складываем цифры, начиная с конца и перенося переполнение в старший разряд

    overflow = 0
    for pos in range(len(s) - 1, -1, -1):
        digit_sum = digit2value[n[pos]] + digit2value[m[pos]] + overflow
        s[pos] = value2digit[digit_sum % BASE]
        overflow = digit_sum // BASE

    # Удаляем из суммы незначащие нули слева
    while len(s) > 1 and s[0] == '0':
        s.popleft()

    return s


def long_hex_prod(a, b):
    """Произведение двух чисел, записанных в деке в виде ['A', '2']"""

    # Длина произведения не превысит суммы длин множителей.
    # Для удобства, сначала в результирующий дек складываем цифры как числа, а не строки
    p = deque([0] * (len(a) + len(b)))

    # Суть в том, что если нумеровать цифры с младших разрядов (т.е. в нашем случае с конца),
    # то произведение i-й цифры первого числа на j-ю цифру второго
    # нужно заносить в (i+j)-ю цифру результата, а если возникло переполнение,
    # гнать его в старшие цифры.
    for i, a_digit in zip(range(len(a)-1, -1, -1), a):
        for j, b_digit in zip(range(len(b)-1, -1, -1), b):
            pos = i + j + 1
            p[-pos] += digit2value[a_digit] * digit2value[b_digit]
            while pos < len(p) and p[-pos] >= BASE:
                p[-pos-1] += p[-pos] // BASE
                p[-pos] = p[-pos] % BASE
                pos += 1

    # Преобразуем цифры-числа в цифры-символы
    p = deque([value2digit[d] for d in p])

    # Удаляем из результата незначащие нули слева
    while len(p) > 1 and p[0] == '0':
        p.popleft()

    return p


if __name__ == '__main__':
    a = deque(input("Введите 1-е шестнадцатеричное число: ").upper())
    b = deque(input("Введите 2-е шестнадцатеричное число: ").upper())
    s = long_hex_sum(a, b)
    p = long_hex_prod(a, b)
    print(f"Сумма = {list(s)}")
    print(f"Произведение = {list(p)}")
    assert s == deque(hex(int(''.join(a), 16) + int(''.join(b), 16)).upper()[2:])
    assert p == deque(hex(int(''.join(a), 16) * int(''.join(b), 16)).upper()[2:])

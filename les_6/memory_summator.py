import sys
from collections import defaultdict


class MemorySummator:

    def __init__(self, *variables):
        self._variables_by_type = defaultdict(lambda: {'cnt': 0, 'bytes_cnt': 0})
        self.count_variables(*variables)

    def count_variables(self, *variables):
        for var in variables:
            self._count_variable(var)

    @property
    def bytes_cnt(self):
        bytes = 0
        for numbers in self._variables_by_type.values():
            bytes += numbers['bytes_cnt']
        return bytes

    def _count_variable(self, var):
        type_dict = self._variables_by_type[type(var)]
        type_dict['cnt'] += 1
        type_dict['bytes_cnt'] += sys.getsizeof(var)

        if hasattr(var, '__iter__'):
            if isinstance(var, dict):
                for k, v in var.items():
                    self._count_variable(k)
                    self._count_variable(v)
            elif not isinstance(var, str):
                for element in var:
                    self._count_variable(element)

    def __str__(self):
        def byte_declination(n):
            """Склоняем байты правильно"""
            if (11 <= n % 100 <= 19 or
                    n % 10 in (0, 1, 5, 6, 7, 8, 9)):
                return 'байт'
            else:
                return 'байта'

        bytes_cnt = self.bytes_cnt

        return (
                f"Переменные заняли в сумме {bytes_cnt} {byte_declination(bytes_cnt)}\n" +
                '\n'.join([f"Объекты класса {type_} в количестве {v['cnt']} "
                           f"заняли {v['bytes_cnt']} {byte_declination(v['bytes_cnt'])}"
                           for type_, v in self._variables_by_type.items()])
        )


# test
test_dict = {1: 'abc', 2: 3.14, 3: [11, 12, 13, 14]}
ms = MemorySummator(test_dict)
assert ms.bytes_cnt == sum(sys.getsizeof(x) for x in (
    test_dict,
    1, 'abc', 2, 3.14, 3, [11, 12, 13, 14],
    11, 12, 13, 14
))

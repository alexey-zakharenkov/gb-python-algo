"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество
различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9

"""

def count_substrings(s, set_class=set):
    """Возвращает количество различных подстрок,
    кроме пустой строки и самой строки.
    """
    substrings = set_class()
    for length in range(1, len(s)):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            substrings.add(substring)
    return len(substrings)


class MySet:

    _START_SIZE = 16
    _MAX_FILL_FACTOR = 4  # Во сколько раз кол-во элементов может превышать размер хеш-таблицы
    _INCREASE_FACTOR = 2  # Во сколько раз увеличивать массив при перехешировании

    def __init__(self, hash_function=hash):
        self._hash_table = [None] * MySet._START_SIZE
        self._hash_function = hash_function
        self._elements_cnt = 0

    def _add(self, table, element):
        """Функция добавления в произвольную хеш-таблицу"""
        h = self._hash_function(element) % len(table)
        if table[h] is None:
            table[h] = []
        bucket = table[h]
        if element not in bucket:
            bucket.append(element)
            return True
        return False

    def remove(self, el):
        raise NotImplementedError("Метод remove() ещё не реализован")

    def add(self, element):
        """Добавление в свою внутреннюю хеш-таблицу"""
        if self._add(self._hash_table, element):
            self._elements_cnt += 1
            if self._elements_cnt > MySet._MAX_FILL_FACTOR * len(self._hash_table):
                self._rehash()

    def _rehash(self):
        """Увеличивает массив и всё перехеширует"""
        new_hash_table = [None] * len(self._hash_table) * MySet._INCREASE_FACTOR
        for el in self:
            self._add(new_hash_table, el)
        self._hash_table = new_hash_table

    def __iter__(self):
        self._bucket_idx = 0
        self._element_idx = 0
        return self

    def __next__(self):
        next_bucket_idx = self._bucket_idx
        next_element_idx = self._element_idx
        while next_bucket_idx < len(self._hash_table):
            if (not self._hash_table[next_bucket_idx] or
                    next_element_idx >= len(self._hash_table[next_bucket_idx])):
                next_bucket_idx += 1
                next_element_idx = 0
                continue
            self._bucket_idx = next_bucket_idx
            self._element_idx = next_element_idx + 1
            return self._hash_table[next_bucket_idx][next_element_idx]
        else:
            raise StopIteration

    def __len__(self):
        return self._elements_cnt


if __name__ == "__main__":
    s = input("Введите строку: ")
    print(f"Различных подстрок с set: {count_substrings(s, set)}")
    print(f"Различных подстрок с MySet: {count_substrings(s, MySet)}")

"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
import sys

from collections import Counter
from pprint import pprint
from queue import PriorityQueue


class HaffmanEncoder:
    """Класс кодирует строку и сохраняет внутри себя таблицу кодов
    для последующего декодирования."""

    def encode(self, s):
        if not s:
            self.symbol_codes = {}
            return ''

        haffman_tree = self._build_haffman_tree(s)
        self._calculate_symbol_codes(haffman_tree)
        bit_string = ''.join(self.symbol_codes[char] for char in s)
        return bit_string

    def decode(self, bit_string):
        if not hasattr(self, 'symbol_codes'):
            raise Exception('Нельзя раскодировать: вы ещё ничего не закодировали')

        # Отложенное получение обратного отображения - кодов в символы
        if not hasattr(self, 'code_symbols'):
            self.code_symbols = {v: k for k, v in self.symbol_codes.items()}

        result = ''
        pos = 0
        while pos < len(bit_string):
            code_len = 1
            while pos + code_len <= len(bit_string):
                next_code = self.code_symbols.get(bit_string[pos:pos + code_len])
                if next_code is not None:
                    result += next_code
                    pos += code_len
                    break
                else:
                    code_len += 1
            else:
                raise Exception("Не нашлось битовой последовательности для раскодирования.\n"
                                "Вероятно, эта битовая строка была испорчена или была\n"
                                "получена другим экземпляром класса HaffmanEncoder.")
        return result

    class HaffmanTreeNode:
        def __init__(self, frequency, symbol=None, left=None, right=None):
            self.frequency = frequency
            self.symbol = symbol
            self.left = left
            self.right = right

        # Сравнение нужно для упорядочения по приоритетам
        def __lt__(self, other):
            return self.frequency < other.frequency

    @staticmethod
    def _build_haffman_tree(s):
        frequencies = Counter(s)
        p_queue = PriorityQueue()

        for symbol, freq in frequencies.items():
            node = HaffmanEncoder.HaffmanTreeNode(freq, symbol=symbol)
            p_queue.put(node)

        while p_queue.qsize() > 1:
            node1 = p_queue.get()
            node2 = p_queue.get()
            combined_node = HaffmanEncoder.HaffmanTreeNode(
                node1.frequency + node2.frequency,
                left=node1,
                right=node2
            )
            p_queue.put(combined_node)

        haffman_tree_root = p_queue.get()
        return haffman_tree_root

    def _calculate_symbol_codes(self, haffman_tree_root):
        """По дереву Хаффмана возвращает таблицу кодов symbol => string of bits"""

        # Случай, когда в строке был только один символ, нуждается в отдельной обработке
        if haffman_tree_root.left is None and haffman_tree_root.right is None:
            self.symbol_codes = {haffman_tree_root.symbol: '0'}
            return

        codes = {}

        def tree_traversal(node, path):
            if node.left is None:
                codes[node.symbol] = path
            else:
                tree_traversal(node.left, path + '0')
                tree_traversal(node.right, path + '1')

        tree_traversal(haffman_tree_root, '')
        self.symbol_codes = codes


if __name__ == "__main__":
    s = 'аббракадаббра'  #input("Введите строку: ")
    haffman = HaffmanEncoder()
    bit_string = haffman.encode(s)
    print(f"Закодированная строка = '{bit_string}'")
    print(f"Степень сжатия {len(s.encode('utf-8')) / (len(bit_string)//8 or 1):.3f}")

    decoded_s = haffman.decode(bit_string)
    print(f"Раскодированная строка = '{decoded_s}'")

    print("\nКодовая таблица:")
    print("\n".join(f"{symbol}: {code}" for symbol, code in haffman.symbol_codes.items()))

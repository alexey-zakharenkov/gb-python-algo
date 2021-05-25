"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число. Проанализировать скорость и
сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

def sieve(n):
    """Найти n-е простое число"""

    # Индекс в массиве is_prime - это число,
    # а значение по индексу - простое ли оно
    is_prime = [False, False] + [None] * 10

    # Все найденные простые числа по порядку
    primes = []

    def extend_is_prime():
        """Так как неизвестно, сколько чисел нужно перебрать, чтобы
        найти n-е простое, то мы периодически расширяем в два раза
        массив is_prime и просеиваем все числа в старшей половине
        уже найденными простыми числами"""
        current_sieve_size = len(is_prime)
        is_prime.extend([None] * current_sieve_size)
        for prime in primes:
            multiple = (current_sieve_size // prime) * prime
            if multiple == prime:
                multiple += prime
            while multiple < len(is_prime):
                is_prime[multiple] = False
                multiple += prime

    while len(primes) < n:
        next_prime = (0 if not primes else primes[-1]) + 1
        while next_prime < len(is_prime):
            if is_prime[next_prime] is None:
                is_prime[next_prime] = True
                primes.append(next_prime)

                multiple = next_prime * 2
                while multiple < len(is_prime):
                    is_prime[multiple] = False
                    multiple += next_prime


                break
            next_prime += 1
        else:
            extend_is_prime()
    #print(primes)
    return primes[-1]


def prime(n):
    primes = []

    next_number = 2
    while len(primes) < n:
        for p in primes:
            if next_number % p == 0:
                break
        else:
            primes.append(next_number)
        next_number += 1

    return primes[-1]


if __name__ == "__main__":
    import timeit
    for f in (sieve, prime):
        for n in (250, 500, 1000, 2000, 4000):
            print(f.__name__, timeit.timeit("f(n)", number=10, globals=globals()))

"""
Цифры и графики - в файле prime_numbers.png

Сложность решета Эратосфена, судя по графику, линейная, а 
сложность обычной проверки на простоту в двойном цикле - квадратичная.
"""

#task 1.4.
# Написать программу, которая выводит на экран первые N простых чисел.
"""
присесть
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def first_n_primes(n):
    primes = []
    candidate = 2
    for i in range(n):
        print(i)

        while not is_prime(candidate):
            candidate += 1
        primes.append(candidate)
        candidate += 1

    return primes


N = int(input("Введите количество простых чисел для вывода: "))
primes = first_n_primes(N)
print(f"Первые {N} простых чисел: {primes}")

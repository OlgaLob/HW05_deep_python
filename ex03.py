#  Создайте функцию генератор чисел Фибоначчи (см. Википедию)

num = int(input('введите число  '))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fib(num)))

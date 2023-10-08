#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc


def fib_python(n):
    if n <= 1:
        return n
    else:
        return fib_python(n - 1) + fib_python(n - 2)


@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n - 1) + fib_numba(n - 2)


def main():

    f = Person(1)
    tid_c = []
    for i in range(1, 5):
        start = pc()
        f.set(i)
        f.fib()
        end = pc()
        tid_c.append(end-start)


    tid_numba = []
    for i in range(30, 40):
        start = pc()
        fib_numba(i)
        end = pc()
        tid_numba.append(end - start)

    tid_python = []
    for i in range(30, 40):
        start = pc()
        fib_python(i)
        end = pc()
        tid_python.append(end - start)

    print(f"tid c: {tid_c}")
    print(f"tid numba: {tid_numba}")
    print(f"tid python: {tid_python}")




if __name__ == '__main__':
    main()

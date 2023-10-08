#!/usr/bin/env python3
import matplotlib.pyplot as plt
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

    """
    tid_c = []
    for i in range(30, 40):
        start = pc()
        f.set(i)
        f.fib()
        end = pc()
        tid_c.append(end - start)

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
    """

    tid_c2 = []
    for i in range(20, 30):
        start = pc()
        f.set(i)
        f.fib()
        end = pc()
        tid_c2.append(end - start)

    tid_numba2 = []
    for i in range(20, 30):
        start = pc()
        fib_numba(i)
        end = pc()
        tid_numba2.append(end - start)

    tid_python2 = []
    for i in range(20, 30):
        start = pc()
        fib_python(i)
        end = pc()
        tid_python2.append(end - start)

    print(f"tid c2: {tid_c2}")
    print(f"tid numba2: {tid_numba2}")
    print(f"tid python2: {tid_python2}")

    """
    # X-axis values (assuming they are 0 through 9)
    x = list(range(10))

    # Plotting the data
    plt.plot(x, tid_c2, label='tid c')
    plt.plot(x, tid_numba2, label='tid numba')
    plt.plot(x, tid_python2, label='tid python')

    # Adding labels and a legend
    plt.xlabel('Index')
    plt.ylabel('Time')
    plt.legend()

    # Display the plot
    plt.show()
    """

    print(fib_numba(47))


if __name__ == '__main__':
    main()

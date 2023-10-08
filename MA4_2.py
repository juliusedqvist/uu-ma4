#!/usr/bin/env python3
import matplotlib.pyplot as plt
# from person import Person
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

    # f = Person(1)

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

    tid_c2 = [0.00012193003203719854, 0.0001884800149127841, 0.00030249200062826276, 0.00048769201384857297,
              0.0007875020382925868, 0.0012824769946746528, 0.0020596369868144393, 0.0033333589672110975,
              0.0053893139702267945, 0.008720298006664962]
    tid_numba2 = [0.43480879900744185, 0.00018638098845258355, 0.00029727094806730747, 0.0004890720010735095,
                  0.0007774480036459863, 0.0012567469966597855, 0.002037527970969677, 0.0032897109631448984,
                  0.00537007802631706, 0.008627108996734023]
    tid_python2 = [0.003943072981201112, 0.006310531985946, 0.010231724998448044, 0.01660600898321718,
                   0.026873217022512108, 0.04340556199895218, 0.07065400801366195, 0.11262412701034918,
                   0.18147030903492123, 0.2923993479926139]

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


    print(fib_numba(47))



if __name__ == '__main__':
    main()

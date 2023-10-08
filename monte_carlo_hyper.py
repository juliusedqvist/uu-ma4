import random, math
from time import perf_counter as pc
import concurrent.futures as future


def monte_carlo_hyper(n, d):
    coords = [[random.uniform(-1, 1) for i in range(n)] for i in range(d)]
    t = [sum([k ** 2 for k in j]) for j in [list(map(lambda x: x[i], coords)) for i in range(n)]]

    inside = [i for i in t if i <= 1]

    return len(inside) / len(t) * 2 ** d


def hyper_volume(r, d):
    return (math.pi ** (d / 2)) / math.gamma(d / 2 + 1) * r ** d


def runner(n):
    return n


def timer(func):
    start = pc()
    n = [runner(func(1000000, 11))] * 10

    with future.ProcessPoolExecutor() as ex:
        results = ex.map(runner, n)

    for r in results:
        print(r)

    end = pc()
    print(f"Process took {round(end - start, 2)} seconds")


# print(hyper_volume(1, 3))
# print(monte_carlo_hyper(10000, 3))

if __name__ == "__main__":

    timer(monte_carlo_hyper)
    start2 = pc()

    # monte_carlo_hyper(10000000, 11)

    end2 = pc()
    print(f"Process took {round(end2 - start2, 2)} seconds")

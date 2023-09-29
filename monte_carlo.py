import math
import random
import matplotlib.pyplot as plt

def monte_carlo_square(n, r):
    circle = []
    square = []
    ret = [(random.uniform(-r, r), random.uniform(-r, r)) for i in range(n)]
    for i in ret:
        if math.sqrt(i[0]**2 + i[1]**2) <= 1:
            circle.append(i)
        else:
            square.append(i)
    print(len(circle))
    print(math.pi)

    x_circle = [i[0] for i in circle]
    y_circle = [i[1] for i in circle]

    x_square = [i[0] for i in square]
    y_square = [i[1] for i in square]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, aspect='equal')

    ax.scatter(x_circle, y_circle, c="red")
    ax.scatter(x_square, y_square, c="blue")

    plt.show()

    return len(circle) / len(ret) * 4

print(monte_carlo_square(1000, 1))

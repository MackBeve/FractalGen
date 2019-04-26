import numpy as np
import matplotlib.pyplot as plt
import random

# currently needs width=height=2^n
# currently uses wrap-around, should adjust for an option to not use in the future.
width = 2048
height = 2048
height_map = np.zeros((width, height))


def diamond_square():
    scale = 1
    step = 64
    for x in range(0, width, step):
        for y in range(0, height, step):
            set_height(x, y, random.uniform(-1 * scale, scale))

    while step > 1:
        halfstep = step / 2
        for x in range(halfstep, width + halfstep, step):
            for y in range(halfstep, height + halfstep, step):
                diamond_step(x, y, halfstep, random.gauss(0, 1) * scale)
        for x in range(0, width, step):
            for y in range(0, height, step):
                square_step(x + halfstep, y, halfstep, random.gauss(0, 1) * scale)
                square_step(x, y + halfstep, halfstep, random.gauss(0, 1) * scale)
        print(step)
        step = step / 2
        scale = scale / 2


def diamond_step(x, y, step, rval):
    a = sample(x - step, y - step)
    b = sample(x + step, y - step)
    c = sample(x - step, y + step)
    d = sample(x + step, y + step)
    set_height(x, y, np.average((a, b, c, d)) + rval)


def square_step(x, y, step, rval):
    a = sample(x - step, y)
    b = sample(x + step, y)
    c = sample(x, y - step)
    d = sample(x, y + step)
    set_height(x, y, np.average((a, b, c, d)) + rval)


def sample(x, y):
    x = x % (width)
    y = y % (height)
    return height_map[x][y]


def set_height(x, y, val):
    x = x % (width)
    y = y % (height)
    height_map[x][y] = val


diamond_square()

plt.imshow(height_map, cmap='Greys')
plt.colorbar()
plt.show()

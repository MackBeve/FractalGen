import numpy as np
import matplotlib.pyplot as plt
import random

delta = np.zeros(8)


def midpoint_bm(vals, maxlevel, sigma=1, seed=""):
    if vals.size != 2 ** maxlevel + 1:
        raise Exception("vals needs to be of size 2^maxlevel + 1")
    for i in range(0, maxlevel):
        delta[i] = sigma * (0.5 ** ((i + 1) / 2))
    n = 2 ** maxlevel
    vals[0] = 0
    vals[n] = sigma * random.gauss(0, 1)
    midpoint_recursion(vals, 0, n, 0, maxlevel)


def midpoint_recursion(vals, index0, index2, level, maxlevel):
    index1 = (index0 + index2) / 2
    if level < maxlevel:
        vals[index1] = 0.5 * (vals[index0] + vals[index2]) + (delta[level] * random.gauss(0, 1))
        midpoint_recursion(vals, index0, index1, level + 1, maxlevel)
        midpoint_recursion(vals, index1, index2, level + 1, maxlevel)


nums = np.zeros(257)
midpoint_bm(nums, 8)
plt.plot(nums)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import random

vals = np.zeros(200)


def white_noise_bm(vals, seed=""):
    vals[0] = 0
    for i in range(1, vals.size):
        # using normal distribution
        vals[i] = vals[i - 1] + random.gauss(0, 1)


white_noise_bm(vals)
plt.plot(vals)
plt.show()

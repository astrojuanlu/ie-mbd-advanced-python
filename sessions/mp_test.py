from time import sleep, monotonic
from multiprocessing import cpu_count, Pool

import numpy as np


def estimate_pi(num_sim):
    """Estimate pi with monte carlo simulation.
    
    Parameters
    ----------
    num_sim: int
        Number of simulations.

    """
    np.random.seed()
    in_circle = 0
    ii = 0
    while ii < num_sim:
        prec_x = np.random.rand()
        prec_y = np.random.rand()

        # Let's use pow here instead of **
        # to see it in the cProfile report
        # x ** 2 + y ** 2 <= 1
        if pow(prec_x, 2) + pow(prec_y, 2) <= 1:
            in_circle += 1  # inside the circle

        ii += 1
        
    return in_circle


if __name__ == "__main__":
    NUM_POINTS = 1e7
    NUM_CORES = cpu_count()

    pool = Pool(NUM_CORES)

    start = monotonic()

    result = pool.map(estimate_pi, [NUM_POINTS / NUM_CORES] * NUM_CORES)
    pi = 4 * sum(result) / NUM_POINTS

    end = monotonic()

    print(result)
    print(pi)
    print(end - start)

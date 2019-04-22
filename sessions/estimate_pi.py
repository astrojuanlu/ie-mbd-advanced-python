import numpy as np


def estimate_pi(num_sim=1e7):
    """Estimate pi with monte carlo simulation.
    
    Parameters
    ----------
    num_sim: int
        Number of simulations.

    """
    in_circle = 0
    ii = 0
    while ii < num_sim:
        prec_x = np.random.rand()
        prec_y = np.random.rand()

        # Let's use pow here instead of **
        # to see it in the cProfile report
        if pow(prec_x, 2) + pow(prec_y, 2) <= 1:
            in_circle += 1  # inside the circle

        ii += 1
        
    return 4 * in_circle / num_sim

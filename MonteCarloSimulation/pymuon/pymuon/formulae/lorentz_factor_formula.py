""".. moduleauthor:: Sacha Medaer"""

import math
import numpy as np


class LorentzFactorFormula():
    """This class compute  the Lorentz factor formula.
    """

    def __init__(self) -> None: # initialize the object's attributes.

        return None

    @staticmethod #what is that?
    def calc_lorentz_factor(rel_velocity):

        if (isinstance(rel_velocity, float) or  isinstance(rel_velocity, int)):
# isinstance checks if rel_velocity is a float or a int
            return math.sqrt(1-rel_velocity**2) # why this formula ?
        else:

            return 1.0 / np.sqrt(1-np.square(rel_velocity)) # real gamma formula


if __name__ == "__main__":
    """This code snippet shows the usage of the class.
    """

    import matplotlib.pyplot as plt
    import numpy as np

    betas = np.linspace(1e-3, 1, 50, False) #(initial value of array, final, number of points in array, not include endpoint)
    gammas = LorentzFactorFormula.calc_lorentz_factor(betas)

    fig, ax1 = plt.subplots()

    ax1.plot(betas, gammas)
    plt.title("Lorentz Factor as a function of the Relativistic Velocity")
    ax1.set_xlabel(r'Relativistic Velocity $\beta$')
    ax1.set_ylabel(r'Lorentz Factor $\gamma$')

    plt.show()

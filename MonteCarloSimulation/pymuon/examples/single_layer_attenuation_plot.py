""".. moduleauthor:: Sacha Medaer"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import physical_constants, c

from pymuon import SingleLayer, Element
import pymuon.utils.utilities as util


symbols = ['Pb', 'Cu', 'Fe', 'He']
# For muon
e_muon = -1
m_muon = physical_constants['muon mass energy equivalent in MeV'][0]   # MeV/c^2


fig, ax1 = plt.subplots()
x = 5e-0    # cm
particle_kin_energy = 100.
nbr_points = 1000

for symbol in symbols:
    elem = Element(symbol)
    layer = SingleLayer(elem, x)

    atts, xs = layer.calc_attenuation(particle_kin_energy, e_muon, m_muon,
                                      nbr_points, True)

    xs = np.hstack((np.zeros(1), xs))
    atts = np.hstack((np.array([particle_kin_energy]), atts))
    ax1.plot(xs, atts, label=symbol)

ax1.legend(fontsize=20)
plt.title("Kinetic Energy as a function of the Medium Depth with "
          "{} MeV initial Kinetic Energy".format(int(particle_kin_energy)),
          size=25)
ax1.set_xlabel(r"Distance (cm)", size=20)
ax1.set_ylabel(r"Kinetic Energy T (MeV)", size=20)
ax1.tick_params(axis='both', labelsize=20)

plt.show()

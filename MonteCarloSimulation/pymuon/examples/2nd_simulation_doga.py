import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import physical_constants, c

from pymuon import SingleLayer, MultiLayers, Element, Compound
import pymuon.utils.utilities as util

media = {}
# Media 1 : Fe
media['Fe'] = Element('Fe')
# Media 2 : Air
media['Air'] = Compound({'N': 0.78, 'O': 0.22})
# Media 3 : Scintillator (e.g. Polyvinyl toluene)
media['Sci'] = Compound({'C': 0.476, 'H': 0.524})
# Media 4 : Pb (Lead)
media['Pb'] = Element('Pb')

color_media = {'Fe': 'orange', 'Air': 'gray', 'Sci': 'silver', 'Pb': 'blue'}

layer_sequence = [('Air', 7.5), ('Fe', 1.0), ('Pb', 1.0), ('Sci', 2.5)] + [('Air', 7.5), ('Fe', 1.0), ('Sci', 2.5)] * 7

# For muon
e_muon = -1
m_muon = physical_constants['muon mass energy equivalent in MeV'][0]   # MeV/c^2
en_muon  = [50., 100., 150., 180., 205.,  250., 300.]  # MeV

fig, ax1 = plt.subplots(figsize=(12, 8))

nbr_points = 10000

for en in en_muon:
    layers = []
    for elem in layer_sequence:
        layers.append(SingleLayer(media[elem[0]], elem[1]))

    multi_layers = MultiLayers(layers)

    atts, xs = multi_layers.calc_attenuation(en, e_muon, m_muon, nbr_points,
                                             True)
    xs = np.hstack((np.zeros(1), xs))
    atts = np.hstack((np.array([en]), atts))

    ax1.plot(xs, atts, label='Muon with {} MeV initial kin. energy'.format(en))

# Add color for different media
start = 0
parsed_compound = []
for i, elem in enumerate(layer_sequence):
    if elem[0] in parsed_compound:
        ax1.axvspan(start, start+elem[1], alpha=0.5, color=color_media[elem[0]])
    else:
        parsed_compound.append(elem[0])
        ax1.axvspan(start, start+elem[1], alpha=0.5,
                    color=color_media[elem[0]], label=elem[0])
    start += elem[1]

# Plot parameters
ax1.legend(fontsize=10, loc='upper right')
plt.title("Kinetic Energy as a function of the Material and Material Depth", size=25)
ax1.set_xlabel(r"Distance (cm)", size=20)
ax1.set_ylabel(r"Kinetic Energy T (MeV)", size=20)
ax1.tick_params(axis='both', labelsize=20)
plt.savefig('adjusted_energy_Pb', dpi=1000, bbox_inches='tight')
plt.show()

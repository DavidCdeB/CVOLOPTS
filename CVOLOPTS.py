#
import re
import os
import glob
from itertools import islice
import numpy as np
import subprocess
import itertools
import sys

# Setting the number of formula units as a raw_input:
n_F_u = raw_input("""

Please type as an integer the number of formula units in the primitive cell. 
For example, Calcite I contains 2 formula units in the primitive (rombohedral) cell and 6 formula units in the crystallographic (hexagonal) cell. Thus, the number to be introduced is:   2 <and press ENTER>

""")

n_F_u = float(n_F_u)
n_F_u = int(float(n_F_u))


ENERGY = []
VOLUME = []

path='./*'
template = os.path.join(path, '*.out')

for fname in glob.glob(template):
  print fname
  f = open(fname, 'r')

  for line in f:

        if 'OPT EN' in line:  
                  print line
                  columns = line.split()
                  print 'columns = ', columns
                  energy = columns[7]
                  print 'energy = ', energy
                  ENERGY.append(energy)
 
        if 'FINAL OPTIMIZED GEOMETRY' in line:  
                  print line
                  parameters = (''.join(islice(f, 4)))
                  print parameters
                  columns2 = parameters.split()
                  print 'columns2 =', columns2
                  volume = columns2[27]
                  print 'volume = ', volume
                  print 'type(volume) = ', type(volume)
                  VOLUME.append(volume)
                    
print 'ENERGY = ', ENERGY 
print 'VOLUME = ', VOLUME

print 'type1  ENERGY = ', type(ENERGY)  #  # At this point these  <type 'list'> are made of
print 'type1  ENERGY[0] = ', type(ENERGY[0])  # <type 'str'> 

ENERGY = [float(i) for i in ENERGY] # Conversion of each element of the list from strings to floats
VOLUME = [float(i) for i in VOLUME]

print 'type2  ENERGY = ', type(ENERGY)  #  At this point these  <type 'list'> are made of
print 'type2  ENERGY[0] = ', type(ENERGY[0])  # <type 'float'> 


# We transform to numpy arrays, because this will better handle data:
ENERGY = np.array(ENERGY)
VOLUME = np.array(VOLUME)

print 'type3  ENERGY = ', type(ENERGY)  # At this point these <type 'numpy.ndarray'> are made of 
print 'type3  ENERGY[0] = ', type(ENERGY[0])  # <type 'numpy.float64'> 


ENERGY_per_f_unit = ENERGY/n_F_u
VOLUME_per_f_unit = VOLUME/n_F_u
print 'ENERGY_per_f_unit =', ENERGY_per_f_unit

output_array = np.vstack((ENERGY, VOLUME, ENERGY_per_f_unit, VOLUME_per_f_unit)).T
np.savetxt('Energy_Volume_grey_triangles.dat', output_array, header = "ENERGY \t     VOLUME \t       ENERGY_per_f_unit \tVOLUME_per_f_unit" , fmt="%0.13f")



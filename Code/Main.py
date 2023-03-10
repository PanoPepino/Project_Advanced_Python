import numpy as np # importing numpy
import time # To check how much time it takes to perform steps. We are dealing with plenty of objects
from itertools import permutations
import Amplitude_Tools #My package to disect and play with amplitudes

## Material to use and definitions

Amplitude = Amplitude_Tools.Read_Amplitude_Func("Long.csv")
Polarisation = ['e1', 'e2', 'e3', 'e4','e5','e6'] # The substring to look at

############################################################################

A = Amplitude_Tools.Selector(Amplitude)
print(A.Looking_for_e_General(Polarisation))






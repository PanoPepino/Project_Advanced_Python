import numpy as np # importing numpy
import time # To check how much time it takes to perform steps. We are dealing with plenty of objects
from itertools import permutations
import Amplitude_Tools #My package to disect and play with amplitudes
import re

## Material to use and definitions



############################################################################

#1 Transform given txt of the most general amplitude to a str

Amplitude = Amplitude_Tools.Read_Amplitude_Func("Long.csv")

#2 Create the class of that Amplitude to extract all relevant terms (writen in another .txt). Define the sub-string relevant to extract (e.e*e.e*e.e) in this case.

General_Amplitude = Amplitude_Tools.Selector(Amplitude)

Polarisation = ['e1', 'e2', 'e3', 'e4','e5','e6'] # The substring to look at
General_Amplitude.Looking_for_e_General(Polarisation)

#3 The Relevant terms have been written in a new .txt file. Define them as the Amplitude piece we are interested.

Relevant_Terms = Amplitude_Tools.Read_Amplitude_Func("Relevant_Terms.txt")
Relevant_Terms = Amplitude_Tools.Selector(Relevant_Terms)
Relevant_Terms.Looking_for_e_Specific(Polarisation, 'A123456.txt')


# To do:
# - Create a permutator that applies the basic substitution rules on Relevant terms.
# - Extract into new files each sub_relevant term for different permutations of the amplitude.
# - Cast all them into the same file.

My_Replacements= {
    "ss1" : "s12",
    "ss2" : "s23",
    "ss3" : "s34",
    "ss4" : "s45",
    "ss5" : "s56",
    "ss6" : "s16",
    "tt1" : "(s12-s34+s56)",
    "tt2" : "(-s12+s34+s56)",
    "tt3" : "(s12+s34-s56)",
  } 
Relevant_Terms_Modified = Amplitude_Tools.Replacetor('Relevant_Terms.txt', My_Replacements, 'Relevant_Terms_Modified.txt')














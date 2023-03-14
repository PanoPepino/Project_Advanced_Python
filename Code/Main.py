import numpy as np # importing numpy
import Amplitude_Tools #My package to disect and play with amplitudes
from Amplitude_Tools import * #There are also function and stuff inside


## Material to use and definitions

############################################################################

#1 Transform given txt of the most general amplitude to a str

Amplitude = Amplitude_Tools.Read_Amplitude_Func("Long.csv")

#2 Create the class of that Amplitude to extract all relevant terms (writen in another .txt). Define the sub-string relevant to extract (e.e*e.e*e.e) in this case.

General_Amplitude = Amplitude_Tools.Selector(Amplitude)
General_Amplitude.Looking_for_e_General(Polarisation)

#3 The Relevant terms have been written in a new .txt file. Define them as the Amplitude piece we are interested.

Relevant_Terms = Amplitude_Tools.Read_Amplitude_Func("Relevant_Terms.txt")
Relevant_Terms = Amplitude_Tools.Selector(Relevant_Terms)
Relevant_Terms.Looking_for_e_Specific(Polarisation, 'A123456.txt')

# To do:
# - Create a permutator that applies the basic substitution rules on Relevant terms.
# - Extract into new files each sub_relevant term for different permutations of the amplitude.
# - Cast all them into the same file.

 
Terms_to_Permute_Try = Amplitude_Tools.Permutator('Relevant_Terms.txt')
Permuted_Terms = Terms_to_Permute_Try.Permuting('136452')
Try = Amplitude_Tools.Selector(Terms_to_Permute_Try)
Try.Looking_for_e_Specific_2(Permuted_Terms, Polarisation, 'Try_Shit.txt')

print(Permuted_Terms[1])



















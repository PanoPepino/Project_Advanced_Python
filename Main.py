import numpy as np # importing numpy
import Amplitude_Tools
from Amplitude_Tools import *
############################################################################

# As an example of how this works, here a description of the steps.

#1 Create the class of that Amplitude to extract all relevant terms (writen in another .txt, inside folder Sequences) using the Selector. The desired reference is in the file "Definitions.py"

General_Amplitude = Amplitude_Tools.Selector('Sequences/Long.csv')
General_Amplitude.Looking_for_e_General(Polarisation)

#2 You may have seen that the Relevant terms (in this case, only those terms that has 6 polarisations e_{i} inside) have been written in a new .txt file in your directory. Now we want to do the following:

#2a Take all those terms and permute them under some rules (calling Permutator). Not only the e_{i} terms will get permuted, but also s_{ij} terms, as they have to do with the momenta of the strings. So string 2 will no longer be number 2 after permuting. Hence, s_{ij} is affected. Let's try permuting under the change '136452'.

Terms_to_Permute= Amplitude_Tools.Permutator('Sequences/Relevant_Terms.txt')
Terms_to_Permute.Permuting('136452', 'Sequences/PT_Example.txt')


#2b Now that we have permuted all those relevant terms, we have to select only some of them. We call the Selector tool again.

Try = Amplitude_Tools.Selector('Sequences/PT_Example.txt')
Try.Looking_for_Specific_Configuration('Sequences/PT_Example.txt', Polarisation)

# This has rewritten the file Permuted_Terms_136452.txt with only those relevant values after permuting (Those that match the desired sequence)

# So Let's make this automatic. We want to explore a set of relevant permutations for our research, given by the following combinations:

Combinations = ['136452', '146352','134625', '143625', '134652', '143652'] # Important terms for our amplitude computation.

for item in Combinations:
    Terms_to_Permute= Amplitude_Tools.Permutator('Sequences/Relevant_Terms.txt')
    Location = 'Sequences/PT_' + item + '.txt'
    Terms_to_Permute.Permuting(item, Location)
    Try = Amplitude_Tools.Selector(Location)
    Try.Looking_for_Specific_Configuration(Location, Polarisation)

# If one now goes to the folder Sequences, there should be six new files. Inside them, only those terms that are relevant for the desired computation.









 























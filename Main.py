import numpy as np # importing numpy
import Amplitude_Tools as AT
from Amplitude_Tools import *
import os

############################################################################

# As an example of how this works, here a description of the steps.

#1 Create the class of that Amplitude to extract all relevant terms (writen in another .txt, inside folder Sequences) using the Selector. The desired reference is in the file "Definitions.py"

General_Amplitude = AT.Selector('Sequences/Long.csv')
General_Amplitude.Looking_for_e_General(Polarisation)

#2 You may have seen that the Relevant terms (in this case, only those terms that has 6 polarisations e_{i} inside) have been written in a new .txt file in your directory. Now we want to do the following:

#2a Take all those terms and permute them under some rules (calling Permutator). Not only the e_{i} terms will get permuted, but also s_{ij} terms, as they have to do with the momenta of the strings. So string 2 will no longer be number 2 after permuting. Hence, s_{ij} is affected. Let's try permuting under the change '136452'.

Terms_to_Permute= AT.Permutator('Sequences/Relevant_Terms.txt')
Terms_to_Permute.Permuting('136452', 'Sequences/PT_Example.txt')

#2b Now that we have permuted all those relevant terms, we have to select only some of them. We call the Selector tool again.

Try = AT.Selector('Sequences/PT_Example.txt')
Try.Looking_for_Specific_Configuration('Sequences/PT_Example.txt')

# This has rewritten the file PT_Example.txt with only those relevant values after permuting (Those that match the desired sequence). Let's make this automatic. We want to explore a set of relevant permutations for our research, given by the following combinations:

Combinations = ['136452', '146352','134625', '143625', '134652', '143652'] # Important terms for our amplitude computation.

for item in Combinations:
    Terms_to_Permute= AT.Permutator('Sequences/Relevant_Terms.txt')
    Location = 'Sequences/Tree_Level/PT_' + item + '.txt'
    Terms_to_Permute.Permuting(item, Location)
    Tree_Level_Terms = AT.Selector(Location)
    Tree_Level_Terms.Looking_for_Specific_Configuration(Location)
    Location_write = 'Sequences/Tree_Level/PT_' + item + '_Together' + '.txt' # Extra lines needed to export the txt in the right way to read in Mathematica.
    with open(Location_write,'w') as f:
        f.write('')
    with open(Location,'r') as firstfile, open(Location_write,'a') as secondfile:
            for line in firstfile:
                secondfile.write(line.strip())
    os.remove(Location) # To remove annoying files lying around.
    

# If one now goes to the folder Sequences/Tree_Level, there should be six new files. Inside them, only those terms that are relevant for the desired computation.
# But we need to go beyond Tree_Level. We need further correction of subpermutations of each element in Combinations. This will be done with the Permute_Subleading method as it is done in the following loop. Inside Sequences, new folder for each element in Combinations will be created and inside each folder, a .txt file for each subpermutation will be written. At the end, the code will read all those files and gather everything in a single file.

for item in Combinations:
    Terms_to_Permute= AT.Permutator('Sequences/Relevant_Terms.txt')
    Extra_Sub_Perm = Terms_to_Permute.Permuting_Subleading(item)
    Location_write = 'Sequences/PT_' + item + '/' + 'AF_' + item + '_Sum' + '.txt'
    with open(Location_write,'w') as f:
        f.write('')
    for jtem in Extra_Sub_Perm:
        Location = 'Sequences/PT_' + item + '/' + 'AF_' + jtem + '.txt'
        Sub_Location = 'Sequences/PT_' + item + '/' + 'AF_' + jtem + 'Mat' + '.txt'
        Sub_Selection = AT.Selector(Location)
        Sub_Selection.Looking_for_Specific_Configuration(Location)
        with open(Sub_Location,'w') as f:
            f.write('')
        with open(Location,'r') as firstfile, open(Location_write,'a') as secondfile: # Extra lines needed to export the txt in the right way to read in Mathematica.
            for line in firstfile:
                secondfile.write(line.strip())
        with open(Location,'r') as firstfile, open(Sub_Location,'a') as secondfile:
            for line in firstfile:
                secondfile.write(line.strip())
        os.remove(Location) # To remove annoying files lying around.














 























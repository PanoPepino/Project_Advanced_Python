import numpy as np # importing numpy
import Amplitude_Tools #My package to disect and play with amplitudes
from Amplitude_Tools import * #There are also function and stuff inside

############################################################################

# As an Example of how this works, here a well described sequence of steps.

#1 Create the class of that Amplitude to extract all relevant terms (writen in another .txt) using the Selector. The desired reference is in the file "Definitions.py"

General_Amplitude = Amplitude_Tools.Selector('Long.csv')
General_Amplitude.Looking_for_e_General(Polarisation)

#2 You may have seen that the Relevant terms (in this case, only those terms that has 6 polarisations e_{i} inside) have been written in a new .txt file in your directory. Now we want to do the following:

#2a Take all those terms and permute them under some rules (calling Permutator). Not only the e_{i} terms will get permuted, but also s_{ij} terms, as they have to do with the momenta of the strings. So string 2 will no longer be number 2 after permuting. Hence, s_{ij} is affected. Let's try permuting under the change '136452'.

Terms_to_Permute_Try = Amplitude_Tools.Permutator('Relevant_Terms.txt')
Permuted_Terms_136452 = Terms_to_Permute_Try.Permuting('136452', 'Permuted_Terms_136452.txt')






## TO DO! CHANGE READ_FUNCT TO NESTED LIST FOR EACH LINE IN THE TXT. THEN, CHANGE CHOPER SO - OR + SPLIT TAKES NO PLACE.






#2b Now that we have permuted all those relevant terms, we have to select only some of them. We call the Selector tool again
Try = Amplitude_Tools.Selector('Permuted_Terms_136452.txt')
cc=Try.Looking_for_Specific_Configuration('Permuted_Terms_136452.txt', Polarisation)




# To do:
# - Create a permutator that applies the basic substitution rules on Relevant terms.
# - Extract into new files each sub_relevant term for different permutations of the amplitude.
# - Cast all them into the same file.

 























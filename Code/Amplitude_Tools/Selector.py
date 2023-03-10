import numpy as np # importing numpy
from itertools import permutations
from .Chopper import *


class Selector(Chop_Tools):
    """
    This class will track down all possible terms in a long chopped sequence (This inherits from Chop_Tools, so it can chop, compare and then, select), and will identify which terms contain a sub-string of parameters. Every term that meets this requirement will be stored in an output array.

    It has several methods:

    Looking_for_e_General
    """
    def __init__(self, Monster):
        Chop_Tools.__init__(self, Monster) #Inherit from Chop_Tools
        self.Monster = Monster

    def Looking_for_e_General(self, Reference):
        """
        This function eats a Reference, which is an array. Then, it copies and splits the Monster (inherited from Chop_Tools) as:

        1) A sequence to inspect, which is the one that should be compared to the reference array.
        2) A sequence to choose from. If one can find the specific reference in 1) the array i where this comparison has taken place will be appended to the chosen ones, which is the output (Only terms in the amplitude which contain the reference)
        """
        Chosen_ones = np.array([])
    
        Sequence_To_Inspect = Chop_Tools(self.Monster).Split_Monster(2)[1]# Split up to each variable.
        Sequence_To_Choose = Chop_Tools(self.Monster).Split_Monster(0)[1] # Split up to terms.

        for i in range(len(Sequence_To_Inspect)):
            for j,value in enumerate(Sequence_To_Inspect[i]): # As we use enumerate (create pairs in the string), we need to add the value counter. 
                sub_string = Sequence_To_Inspect[i][j:len(Reference)+j] # Piece to be read
                sub_string.sort()
                if sub_string == Reference: # If the piece being read coincides with the reference one, add it to chosen ones.
                    Chosen_ones = np.append(Chosen_ones,Sequence_To_Choose[i])
        

        return Chosen_ones
    


    # CONTINUE WORKING HERE ON LOOKING FOR SPECIFIC AFTER HAVING CHOSEN RESPECT TO REFERENCE
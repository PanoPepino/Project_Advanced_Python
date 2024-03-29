import numpy as np # importing numpy
from .Chopper import *
from .Important_Functions import *


class Selector(Chopper):
    """
    This class will track down all possible terms in a long chopped sequence (This inherits from Chop_Tools, so it can chop, compare and then, select), and will identify which terms contain a sub-string of parameters. Every term that meets this requirement will be stored in an output array.

    It has two methods:

    Looking_for_e_General, Looking_for_Specific_Configuration
    """

    def __init__(self, Monster):
        Chopper.__init__(self, Monster) #Inherit from Chop_Tools
        self.Monster = Monster

    def Looking_for_e_General(self, Reference):
        """
        This function eats a Reference, which is an array. Then, it copies and splits the Monster (inherited from Chop_Tools) as:

        1) A sequence to inspect, which is the one that should be compared to the reference array.
        2) A sequence to choose from. If one can find the specific reference in 1) the array [i] where this comparison has taken place will be appended to the chosen ones, which is the output (Only terms in the amplitude which contain the reference). Chosen ones would also be stored as a Relevant_Terms.txt for easier access in the future.
        
        return a .txt file with the chosen lines.
        """

        Chosen_ones = np.array([])
        Chosen_ones_output= np.array([])
    
        Split_Final = Chopper(self.Monster).Split_Monster(2)[1]# Split up to each variable.
        Sequence_To_Choose = Chopper(self.Monster).Split_Monster(0) # Split up to terms.

        for i in range(len(Split_Final)):
            for j,value in enumerate(Split_Final[i]): # As we use enumerate (create pairs in the string), we need to add the value counter. 
                sub_string = Split_Final[i][j:len(Reference)+j] # Piece to be read
                sub_string.sort()
                if sub_string == Reference: # If the piece being read coincides with the reference one, add it to chosen ones.
                    Chosen_ones = np.append(Chosen_ones,Sequence_To_Choose[1][i])
                    Chosen_ones_output = np.append(Chosen_ones_output,(Sequence_To_Choose[0][i],Sequence_To_Choose[1][i]))
                    with open('Sequences/Relevant_Terms.txt', 'w') as f:
                        for item1, item2 in zip(Chosen_ones_output[::2], Chosen_ones_output[1::2]):
                            f.writelines(item1)
                            f.writelines(' ') # So the Read_Function can understand each space with a new entry.
                            f.writelines(item2)
                            f.write('\n')

    def Looking_for_Specific_Configuration(self, Name_file_extension):
        """
        This function eats a file.

        The input file is then chopped down to all variables. They are written in the Split_Final array (quite similar to the chopper tool) Then, each term is inspected up to the first 6 entries and sorted. This is due to the fact that combinations of e.e (Polarisations in this case) are symmetric. So it does not matter if e1.e2 or e2.e1. They are the same. When this sorting by pairs has been performed, that term is then compared to the desired Reference. If they match, the non-chopped term where it can from will be stored in a selected list of chosen terms.

        Finally, all these selected terms will be printed out in the .txt whose name has been indicated in the input of the function.
        """
        
        Output = np.array([])
        
        Pol_2 = [['e1', 'e2'], ['e3', 'e4'], ['e5', 'e6']]
        aa = list(itertools.permutations(Pol_2))
        Iterations_List = []
        for item in aa:
            bb= np.array(item)
            tt=bb.flatten()
            tt= list(tt)
            Iterations_List.append(tt)

        Split_Final = Chopper(Name_file_extension).Split_Monster(2)[1]# Split up to each variable.
        Sequence_To_Choose = Chopper(Name_file_extension).Split_Monster(0) # Split up to terms.

        for i in range(len(Split_Final)):
            Chosen_ones_output = np.array([])
            for j in range(len(Split_Final[i][:3])): # As we use enumerate (create pairs in the string), we need to add the value counter. 
                sub_string = Split_Final[i][2*j:2*j+2] # Piece to be read
                sub_string.sort()
                Chosen_ones_output = np.append(Chosen_ones_output,sub_string)
                Something = Chosen_ones_output.ravel().tolist()

                if Something in Iterations_List: # If the piece being read coincides with the reference one, add it to chosen ones.
                    Output = np.append(Output,(Sequence_To_Choose[0][i],Sequence_To_Choose[1][i]))
                    with open(Name_file_extension, 'w') as f:
                        for item1, item2 in zip(Output[::2], Output[1::2]):
                            f.writelines(item1)
                            f.writelines(' ')
                            f.writelines(item2.replace('$','^-'))
                            f.write('\n')
        

            
                 
                
    

                    
        
    
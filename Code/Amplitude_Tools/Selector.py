import numpy as np # importing numpy
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
        2) A sequence to choose from. If one can find the specific reference in 1) the array [i] where this comparison has taken place will be appended to the chosen ones, which is the output (Only terms in the amplitude which contain the reference). Chosen ones would also be stored as a Relevant_Terms.txt for easier access in the future.
        """

        Chosen_ones = np.array([])
        Chosen_ones_output= np.array([])
    
        Split_Final = Chop_Tools(self.Monster).Split_Monster(2)[1]# Split up to each variable.
        Sequence_To_Choose = Chop_Tools(self.Monster).Split_Monster(0) # Split up to terms.

        for i in range(len(Split_Final)):
            for j,value in enumerate(Split_Final[i]): # As we use enumerate (create pairs in the string), we need to add the value counter. 
                sub_string = Split_Final[i][j:len(Reference)+j] # Piece to be read
                sub_string.sort()
                if sub_string == Reference: # If the piece being read coincides with the reference one, add it to chosen ones.
                    Chosen_ones = np.append(Chosen_ones,Sequence_To_Choose[1][i])
                    Chosen_ones_output = np.append(Chosen_ones_output,(Sequence_To_Choose[0][i],Sequence_To_Choose[1][i]))
                    with open('Relevant_Terms.txt', 'w') as f:
                        for item1, item2 in zip(Chosen_ones_output[::2], Chosen_ones_output[1::2]):
                            f.writelines(item1)
                            f.writelines(item2)
                            f.write('\n')

    def Looking_for_Specific_Configuration(self, List_Input, Reference, Name_file_extension):
        """
        This function eats:
        1) an input list, which will normally come from the Permutator class. 
        2) A reference, which is the substring to look at. For example, my desired polarisation array.
        3) The name of the file where you want to write down those terms that match your requirements.

        The input list is then chopped down to all variables. They are written in the Split_Final array (quite similar to the chopper tool) Then, each term is inspected up to the first 6 entries and sorted. This is due to the fact that combinations of e.e (Polarisations in this case) are symmetric. So it does not matter if e1.e2 or e2.e1. They are the same. When this sorting by pairs has been performed, that term is then compared to the desired Reference. If they match, the non-chopped term where it can from will be stored in a selected list of chosen terms.

        Finally, all these selected terms will be printed out in the file whose name has been indicated in the input of the function.
        """
        
        Split_Pieces_in_Terms = list()
        Split_Final = list()
        Output = np.array([])

        for i in range(len(List_Input[1])): # Loop to split each term into the pieces separated by multiplication
            Split_Pieces_in_Terms.append(List_Input[1][i].split('*'))
    
        for j in range(len(Split_Pieces_in_Terms)): # These 2 loops are to split each piece into variables e_{i} and similar. It also creates a list where all the variables will be nested, which correspond to the term j.
            term_j= list()
            for i in range(len(Split_Pieces_in_Terms[j])):
                bb = Split_Pieces_in_Terms[j][i].split('.')
                for elem in bb:
                    term_j.append(elem)
            Split_Final.append(term_j)

        for i in range(len(Split_Final)):
            Chosen_ones_output = np.array([])
            for j in range(len(Split_Final[i][:3])): # As we use enumerate (create pairs in the string), we need to add the value counter. 
                sub_string = Split_Final[i][2*j:2*j+2] # Piece to be read
                sub_string.sort()
                Chosen_ones_output = np.append(Chosen_ones_output,sub_string)
                Something = Chosen_ones_output.ravel().tolist()

                if Something == Reference: # If the piece being read coincides with the reference one, add it to chosen ones.
                    Output = np.append(Output,(List_Input[0][i],List_Input[1][i]))
                    with open(Name_file_extension, 'w') as f:
                        for item1, item2 in zip(Output[::2], Output[1::2]):
                            f.writelines(item1)
                            f.writelines(item2)
                            f.write('\n')
    

                    
        
    
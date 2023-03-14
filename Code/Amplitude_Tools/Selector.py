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
    
        Sequence_To_Inspect = Chop_Tools(self.Monster).Split_Monster(2)[1]# Split up to each variable.
        Sequence_To_Choose = Chop_Tools(self.Monster).Split_Monster(0) # Split up to terms.

        for i in range(len(Sequence_To_Inspect)):
            for j,value in enumerate(Sequence_To_Inspect[i]): # As we use enumerate (create pairs in the string), we need to add the value counter. 
                sub_string = Sequence_To_Inspect[i][j:len(Reference)+j] # Piece to be read
                sub_string.sort()
                if sub_string == Reference: # If the piece being read coincides with the reference one, add it to chosen ones.
                    Chosen_ones = np.append(Chosen_ones,Sequence_To_Choose[1][i])
                    Chosen_ones_output = np.append(Chosen_ones_output,(Sequence_To_Choose[0][i],Sequence_To_Choose[1][i]))
                    with open('Relevant_Terms.txt', 'w') as f:
                        for item1, item2 in zip(Chosen_ones_output[::2], Chosen_ones_output[1::2]):
                            f.writelines(item1)
                            f.writelines(item2)
                            f.write('\n')
    
    def Looking_for_e_Specific(self, Reference, Name_file_extension):
        """
        CHANGE THIS!!!
        This function eats a Reference (array) and the name of the file we want to create. Then, it copies and splits the Monster (inherited from Chop_Tools) as:

        1) A sequence to inspect, which is the one that should be compared to the reference array.
        2) A sequence to choose from. If one can find the specific reference in 1) the array i where this comparison has taken place will be appended to the chosen ones, which is the output (Only terms in the amplitude which contain the reference). Chosen ones would also be stored as a Name_file.txt for easier access in the future.

        OBS! In this case, as it is specific, we have to remove the sort, as we are interested only on specific sequences of the substring.
        """
        
        Chosen_ones = np.array([])
        Chosen_ones_output= np.array([])
    
        Sequence_To_Inspect = Chop_Tools(self.Monster).Split_Monster(2)[1]# Split up to each variable.
        Sequence_To_Choose = Chop_Tools(self.Monster).Split_Monster(0) # Split up to terms.

        for i in range(len(Sequence_To_Inspect)):
            for j,value in enumerate(Sequence_To_Inspect[i]): # As we use enumerate (create pairs in the string), we need to add the value counter. 
                sub_string = Sequence_To_Inspect[i][j:len(Reference)+j] # Piece to be read
                if sub_string == Reference: # If the piece being read coincides with the reference one, add it to chosen ones.
                    Chosen_ones = np.append(Chosen_ones,Sequence_To_Choose[1][i])
                    Chosen_ones_output = np.append(Chosen_ones_output,(Sequence_To_Choose[0][i],Sequence_To_Choose[1][i]))
                    with open(Name_file_extension, 'w') as f:
                        for item1, item2 in zip(Chosen_ones_output[::2], Chosen_ones_output[1::2]):
                            f.writelines(item1)
                            f.writelines(item2)
                            f.write('\n')

    def Looking_for_e_Specific_2(self, List_Input, Reference, Name_file_extension):
        """
        CHANGE THIS!!!
        """
        ## CHECK THIS!!!!!!!
        Chosen_ones = np.array([])
        Chosen_ones_output= np.array([])
        Split_Pieces_in_Terms = list()
        Split_Final = list()

        for i in range(len(List_Input[1])): # Loop to split each term into the pieces separated by multiplication
            Split_Pieces_in_Terms.append(List_Input[1][i].split('*'))
    
        for j in range(len(Split_Pieces_in_Terms)): # These 2 loops are to split each piece into variables e_{i} and similar. It also creates a list where all the variables will be nested, which correspond to the term j.
            term_j= list()
            for i in range(len(Split_Pieces_in_Terms[j])):
                bb = Split_Pieces_in_Terms[j][i].split('.')
                for elem in bb:
                    term_j.append(elem)
            Split_Final.append(term_j)
    
        Sequence_To_Inspect = Split_Final# Split up to each variable.
        Sequence_To_Choose = List_Input[1] # Split up to terms.

        for i in range(len(Sequence_To_Inspect)):
            for j,value in enumerate(Sequence_To_Inspect[i]): # As we use enumerate (create pairs in the string), we need to add the value counter. 
                sub_string = Sequence_To_Inspect[i][j:len(Reference)+j] # Piece to be read
                if sub_string == Reference: # If the piece being read coincides with the reference one, add it to chosen ones.
                    Chosen_ones = np.append(Chosen_ones,Sequence_To_Choose[1][i])
                    Chosen_ones_output = np.append(Chosen_ones_output,(Sequence_To_Choose[0][i],Sequence_To_Choose[1][i]))
                    with open(Name_file_extension, 'w') as f:
                        for item1, item2 in zip(Chosen_ones_output[::2], Chosen_ones_output[1::2]):
                            f.writelines(item1)
                            f.writelines(item2)
                            f.write('\n')

                    
        
    
import numpy as np
from .Selector import *
from .Chopper import *
from .Definitions import *
from .Important_Functions import *
import os

class Permutator (object):
    """
    This class does the following:

    1) Eats a file and read with Read_Amplitude_Func.
    2) Eats an order in the permutations.
    3) Perform the permutation in each of the relevant terms.
    4) It returns an array with the permuted terms.

    Three methods: 
    
    Replacement_Dict_Creator, Permuting, Permuting_Subleading.
    """

    def __init__(self, Name_File_Input):
        self.Name_File_Input = Name_File_Input
        self.To_Replace = Chopper(Name_File_Input).Split_Monster(0)
    
    def Replacement_Dict_Creator(self, Desired_Permutation):
        """
        This method eats a desired permutation (string) and crafts two dictionaries with replacements that will applied using the replacetor.

        It returns two Dictionaries: Dict_Perm_Pol, Dict_Perm_Mom
        """

        Perm = [*Desired_Permutation]
        Momenta = ['s12', 's23', 's34', 's45', 's56','s16']
        Dict_Perm_Pol = {}
        Dict_Perm_Mom = {}

        for i in range(len(Perm)):
            Dict_Perm_Pol.update({Polarisation[i] : 'e' + str(Perm[i])})

        for j in range(len(Momenta)):
            Entries = [Perm[j], Perm[(j+1) % len(Momenta)]]
            Entries.sort()
            Dict_Perm_Mom.update({Momenta[j] :'s' + str(Entries[0]) + str(Entries[1])})
        
        Dict_Perm_Mom.update({'s13': 's' + str(Perm[0]) + str(Perm[2])})
        Dict_Perm_Mom.update({'s24': 's' + str(Perm[1]) + str(Perm[3])})
        Dict_Perm_Mom.update({'s35': 's' + str(Perm[2]) + str(Perm[4])})

        return Dict_Perm_Pol, Dict_Perm_Mom

    def Permuting (self, Desired_Permutation, Name_file_extension):
        """
        This function eats the desired permutation string and a file input, which will be transformed according to defined rules. It creates directories in case they do not exist. Results are written in the same file.
        """

        # Directory
        directory = 'Tree_Level'
  
        # Parent Directory path
        parent_dir = "/Users/Panizo/CloudDocs/University/Ph.D./Subjects/Advanced_Python_stuff (3)/Project_Advanced_Python/Sequences"
  
        # Path
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.makedirs(path)

        # Eat the txt and replace ss and tt with basic stuff.
        First_Replacement= Replacetor(self.To_Replace[1], Basic_Replacements)

       ## ADD HERE LINES TO ITERATE OVER SUB-PERMUTATIONS AND CREATE FOLDERS FOR EACH PERMUTATION WITH FILES INSIDE FOR EACH SUB-PERMUTATION.
              
        # Now, Given the Desired permutation, Create two dictionaries, one for polarisation changes and another one for momenta
        Creating_Dictionaries = self.Replacement_Dict_Creator(Desired_Permutation)

        # With those two dictionaries in hand, time to replace again.
        Second_Replacement = Replacetor(First_Replacement, Creating_Dictionaries[0])
        Third_Replacement = Replacetor(Second_Replacement, Creating_Dictionaries[1])
        Fourth_Replacement = Replacetor(Third_Replacement, Extra_Replacements)

        with open(Name_file_extension, 'w') as f:
                        for item1, item2 in zip(self.To_Replace[0], Fourth_Replacement):
                            f.writelines(item1)
                            f.writelines(' ')
                            f.writelines(item2)
                            f.write('\n')

    def Permuting_Subleading (self, Desired_Permutation):
        """
        This function eats the desired permutation string, applies Sub_Permutator func to create subpermutations and transform the Monster input (Which will be read from Name file input of the class) according to defined rules. It creates directories in case they do not exist. Results are written in sub files.

        It returns a lists of all subpermutations of the Desired_Permutation input.
        """

        # Directory
        directory = 'PT_' + Desired_Permutation
  
        # Parent Directory path
        parent_dir = "/Users/Panizo/CloudDocs/University/Ph.D./Subjects/Advanced_Python_stuff (3)/Project_Advanced_Python/Sequences"
  
        # Path
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.makedirs(path)

        Second_Order_Desired_Perm = Sub_Permutator(Desired_Permutation)[0]
        F_terms = Sub_Permutator(Desired_Permutation)[1]

        for k in range(len(Second_Order_Desired_Perm)):
            Add_F_Term = []
            for i in range(len(self.To_Replace[1])):
                Plus_F = self.To_Replace[1][i] + '*' + F_terms[k] 
                Add_F_Term.append(Plus_F)

            # Eat the txt and replace ss and tt with basic stuff.
            Zeroth_Replacement = Replacetor(Add_F_Term, F_Replacements)
            First_Replacement= Replacetor(Zeroth_Replacement, Basic_Replacements)

            # Now, Given the Desired permutation, Create two dictionaries, one for polarisation changes and another one for momenta
            Creating_Dictionaries = self.Replacement_Dict_Creator(Second_Order_Desired_Perm[k])

            # With those two dictionaries in hand, time to replace again.
            Second_Replacement = Replacetor(First_Replacement, Creating_Dictionaries[0])
            Third_Replacement = Replacetor(Second_Replacement, Creating_Dictionaries[1])
            Fourth_Replacement = Replacetor(Third_Replacement, Extra_Replacements)

            # Creating the Folder and the file
            Where = path + '/' + 'AF_' + Second_Order_Desired_Perm[k] + '.txt'

            with open(Where, 'w') as f:
                  for item1, item2 in zip(self.To_Replace[0], Fourth_Replacement):
                    f.writelines(item1)
                    f.writelines(' ')
                    f.writelines(item2)
                    f.write('\n')
        return Second_Order_Desired_Perm

        

        





         



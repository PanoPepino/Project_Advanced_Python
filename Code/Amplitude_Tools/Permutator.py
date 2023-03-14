import numpy as np
from .Selector import *
from .Chopper import *
from .Definitions import *
from .Replacetor import *

class Permutator (object):
    """
    This class does the following:

    1) Eats a set of relevant terms.
    2) Eats an order in the permutations
    3) Perform the permutation in each of the relevant terms
    4) Spits out a file with only those terms that match the permutation.

    CONTINUE EXPLAINING
    """
    def __init__(self, Name_File_Input):
        self.Name_File_Input = Name_File_Input
        self.Terms = Read_Amplitude_Func(Name_File_Input)
        self.To_Replace = Chop_Tools(self.Terms).Split_Monster(0)
    
    def Replacement_Dict_Creator(self, Desired_Permutation):
        """
        This method eats a desired permutation (string) and crafts two dictionaries with replacements that will applied using the replacetor.
        """

        Perm = [*Desired_Permutation]
        Momenta = ['s12','s23', 's34', 's45', 's56','s16']

        Dict_Perm_Pol = {}
        Dict_Perm_Mom = {}

        for i in range(len(Perm)):
            Dict_Perm_Pol.update({Polarisation[i] : 'e' + str(Perm[i])})

        for j in range(len(Momenta)):
            Entries = [Perm[j], Perm[(j+1) % len(Momenta)]]
            Entries.sort()
            Dict_Perm_Mom.update({Momenta[j] :'s' + str(Entries[0]) + str(Entries[1])})

        return Dict_Perm_Pol, Dict_Perm_Mom



    def Permuting (self, Desired_Permutation):
        """
        This function eats the desired permutation string and transform the Monster input (Which will be read from Name file input) according to defined rules.
        """
        # Eat the txt and replace ss and tt with basic stuff.
        First_Replacement= Replacetor(self.To_Replace[1], Basic_Replacements)

        # Now, Given the Desired permutation, Create two dictionaries, one for polarisation changes and another one for momenta
        Creating_Dictionaries = self.Replacement_Dict_Creator(Desired_Permutation)

        # With those two dictionaries in hand, time to replace again.
        Second_Replacement = Replacetor(First_Replacement, Creating_Dictionaries[0])
        Third_Replacement = Replacetor(Second_Replacement, Creating_Dictionaries[1])

        return self.To_Replace[0],Third_Replacement




         



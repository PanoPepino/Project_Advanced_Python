import numpy as np

from .Selector import *
from .Chopper import *

class Permutator (Selector):
    """
    This class does the following:

    1) Eats a set of relevant terms.
    2) Eats an order in the permutations
    3) Perform the permutation in each of the relevant terms
    4) Spits out a file with only those terms that match the permutation.

    CONTINUE EXPLAINING
    """
    def __init__(self, Monster):
        Selector.__init__(self, Monster)
        self.Monster = Monster

    def Permuting (self, Desired_Permutation):
        """
        This function eats the desired permutation string and transform the Monster input according to defined rules.
        """


    ## CONTINUE THINKING ABOUT THIS SHIT
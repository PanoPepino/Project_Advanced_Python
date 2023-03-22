import numpy as np
import re
from .Important_Functions import *
from .Chopper import *

def Replacetor(Input_List, Replacements):
   """
   This function eats:

   1) An input list with terms to be replaced.
   2) Replacements (which is a dictionary), that tells you how to perform the replacement of different substring pieces.

   It returns replaced terms as a list.
   """

   Replaced_List = list()
   
   for item in Input_List:
      # Create a regular expression from the dictionary
      regex = re.compile("(%s)" % "|".join(map(re.escape, Replacements.keys())))
      # For each match, look-up corresponding value in dictionary
      Replaced_Term = regex.sub(lambda mo: Replacements[mo.string[mo.start():mo.end()]], str(item))
      Replaced_List.append(str(Replaced_Term))

   
   return Replaced_List
     

   

    
    
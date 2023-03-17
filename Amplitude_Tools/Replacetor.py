import numpy as np
import re
from .Read_Amplitude import *
from .Chopper import *

def Replacetor(Input_List, Replacements):
   """
   This function eats:
   1) An input file with terms to be replaced, that one has extracted with the selector tool.
   2) Replacements (which is a dictionary), that tells you how to perform the replacement of different substring pieces.

   This function will eat terms in a txt format, read through, perform substitutions and spit them out in a new file.
   """

   Replaced_List = list()
   
   for item in Input_List:
      # Create a regular expression from the dictionary
      regex = re.compile("(%s)" % "|".join(map(re.escape, Replacements.keys())))
      # For each match, look-up corresponding value in dictionary
      Replaced_Term = regex.sub(lambda mo: Replacements[mo.string[mo.start():mo.end()]], str(item))
      Replaced_List.append(str(Replaced_Term))

   
   return Replaced_List
     

   

    
    
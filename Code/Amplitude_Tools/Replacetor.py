import numpy as np
import re
from .Read_Amplitude import *
from .Chopper import *

def Replacetor(Name_File_Input, Replacements, Name_File_Ouput):
   """
   This function eats:
   1) An input file with terms to be replaced, that one has extracted with the selector tool.
   2) Replacements (which is a dictionary), that tells you how to perform the replacement of different substring pieces.
   3) An ouput file, which is the document that will be created to host those terms that has been massaged.

   This function will eat terms in a txt format, read through, perform substitutions and spit them out in a new file.
   """
   Terms = Read_Amplitude_Func(Name_File_Input)

  

   To_Replace = Chop_Tools(Terms).Split_Monster(0)

   with open(Name_File_Ouput,'w') as text:
      for item1, item2 in zip(To_Replace[0],To_Replace[1]):
          # Create a regular expression  from the dictionary keys
          regex = re.compile("(%s)" % "|".join(map(re.escape, Replacements.keys())))#¢# For each match, look-up corresponding value in dictionary
          Replaced_Terms = regex.sub(lambda mo: Replacements[mo.string[mo.start():mo.end()]], item2)
          text.writelines(item1)
          text.writelines(Replaced_Terms)
          text.write('\n')
   

   

    
    
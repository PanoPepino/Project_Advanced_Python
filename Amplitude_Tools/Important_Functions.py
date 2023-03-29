import numpy as np
import re
import itertools

def Read_Amplitude_Func(Name_file_extension):
    """
    This function eats file.csv or .txt file and spits out a string that the system can read.

    It returns the read file as a np.array.
    """

    Amplitude= np.genfromtxt(Name_file_extension, dtype='str', delimiter=' ')

    return Amplitude


def Replacetor(Input_List, Replacements):
   """
   This function eats two arguments:

   1) An input list with terms to be replaced.
   2) Replacements (which is a dictionary), that tells you how to perform the replacement of different substring pieces.

   It returns the replaced list.
   """

   Replaced_List = list()
   
   for item in Input_List:
      # Create a regular expression from the dictionary
      regex = re.compile("(%s)" % "|".join(map(re.escape, Replacements.keys())))
      # For each match, look-up corresponding value in dictionary
      Replaced_Term = regex.sub(lambda mo: Replacements[mo.string[mo.start():mo.end()]], str(item))
      Replaced_List.append(str(Replaced_Term))

   return Replaced_List

def Sub_Permutator (String_Input):
    """
    This function eats a string input (argument) and choose its second, third and fourth entry. Then, it will permute these 3 entries and create sub-permutation strings associated with F-terms, that will be substituted later.

    It returns two lists: Sub_Perm and F_Perm.
    """

    Sub_Perm = []
    F_Perm = []
    Permu = [*String_Input]
    Sub_string = list(itertools.permutations (Permu[1:4]))
    Sub_string_Pos = list(itertools.permutations ([Permu[1],Permu[2],Permu[3]]))
    for i in range(len(Sub_string)):
        To_Rewrite = Sub_string[i][0] + Sub_string[i][1] + Sub_string[i][2]
        F_To_Rewrite = 'F' + Sub_string_Pos[i][0] + Sub_string_Pos[i][1] + Sub_string_Pos[i][2]
        Result = Permu[0] + To_Rewrite + Permu[4] + Permu[-1]
        Sub_Perm.append(Result)
        F_Perm.append(F_To_Rewrite)
    
    For_F = []
    for item in Sub_Perm:
        For_F.append([*item])
    
    return Sub_Perm, F_Perm, For_F

def Oli_Corrections(Some_Permutation):
    """
    This function eats a permutation crafts a list of specific corrections computed by Oliver, up to alpha^{2} level.

    Args:
        Some_Permutation (String)
    Output:
        List
    """
    
    Permu = [*Some_Permutation]
    Corr234 = 'mZeta[2]*(' + 's' + Permu[3] + Permu[4] + '*s' + Permu[4] + Permu[5] + '+s' + Permu[0] + Permu[1] + '*s' + Permu[-1] + Permu[0] + '-s' + Permu[3] + Permu[4] + '*(' + 's' + Permu[0] + Permu[1] + '+s'  + Permu[0] + Permu[2] + '+s' + Permu[1] + Permu[2] + ')' + '-s' + Permu[0] + Permu[1] + '*(' + 's' + Permu[2] + Permu[3] + '+s' + Permu[2] + Permu[4] + '+s' + Permu[3] + Permu[4] +')' + '+' + '(' + 's' + Permu[0] + Permu[1] + '+s'  + Permu[0] + Permu[2] + '+s' + Permu[1] + Permu[2] + ')' + '*' +  '(' + 's' + Permu[2] + Permu[3] + '+s' + Permu[2] + Permu[4] + '+s' + Permu[3] + Permu[4] +')'+')'
    Corr243 = 'mZeta[2]*(' + 's' + Permu[2] + Permu[4] + '*(s' + Permu[2] + Permu[3] +'-s' + Permu[4] + Permu[5] +'+(' + 's' + Permu[0] + Permu[1] + '+s' + Permu[0] + Permu[2] + '+s' + Permu[1] + Permu[2] + ')'+')'+')'
    Corr324 = 'mZeta[2]*(' + 's' + Permu[0] + Permu[2] + '*(' + 's' + Permu[1] + Permu[2] + '-s' + Permu[-1] + Permu[0] + '+(s' + Permu[2] + Permu[3] + '+s' + Permu[2] + Permu[4] + '+s' + Permu[3] + Permu[4] + ')' + ')'+')'
    Corr342 = 'Zeta[2]*(' + 's' + Permu[0] + Permu[2] + '*s' + Permu[1] + Permu[4] + ')'
    Corr423 = 'Zeta[2]*(' + 's' + Permu[0] + Permu[3] + '*s' + Permu[2] + Permu[4] + ')'
    Corr432 = 'mZeta[2]*(' + 's' + Permu[0] + Permu[3] + '*s' + Permu[1] + Permu[4] + ')'
    
    return Corr234, Corr243, Corr324, Corr342, Corr423, Corr432
    
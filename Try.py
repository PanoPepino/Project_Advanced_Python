import numpy as np
import itertools



def Sub_Permutator (String_Input):
    Sub_Perm = []
    F_Perm = []
    Perm = [*String_Input]
    Sub_string = list(itertools.permutations (Perm[1:4]))
    Sub_string_Pos = list(itertools.permutations (['2','3','4']))
    for i in range(len(Sub_string)):
        To_Rewrite = Sub_string[i][0] + Sub_string[i][1] + Sub_string[i][2]
        F_To_Rewrite = 'F' + Sub_string_Pos[i][0] + Sub_string_Pos[i][1] + Sub_string_Pos[i][2]
        Result = Perm[0] + To_Rewrite + Perm[4] + Perm[-1]
        Sub_Perm.append(Result)
        F_Perm.append(F_To_Rewrite)
    
    return Sub_Perm, F_Perm

print(Sub_Permutator('136452'))

    


import numpy as np # importing numpy
from itertools import permutations


## Good day, curious traveller. In this file, we will define all necessary functions to will be used in our travel around the Amplitude world. Do not despair, as things can be manipulated quite easy. We will start with the following function.


def Split_Monster(Monster, number): # This function eats a string and chop it as specifies as follows:

    # number == 0, it will chop each term of the string and spit out signs in 1 array and terms in other.
    # number == 1, it will chop further the terms and divide in multiplication
    # number == 2, it will go further and isolate each variable in each term

    Split_Terms=np.array([]) # Empty array to split further those minuses
    Split_Pieces_in_Terms=list()
    Split_Final=list() # Empty array to split further those minuses
    Signs_match=np.array(['']) # Array whose 0th entry is a space, will go in front of first term of sequence. Do not ask. Python issue.
    
    # This next 2 lines take care of splitting the string you want to break and extracts
    
    Split_First_Plus = Monster.split('+') # Split will separate previous string into only terms for each plus that reads through
    for i in range(len(Split_First_Plus)):# Loop that takes care of minuses
        Split_Terms=np.append(Split_Terms,Split_First_Plus[i].split('-'))
 
    for i in range(len(Split_Terms)): # Loop to split each term into the pieces separated by multiplication
            Split_Pieces_in_Terms.append(Split_Terms[i].split('*'))
    
    for j in range(len(Split_Pieces_in_Terms)): # These 2 loops are to split each piece into variables e_{i} and similar. It also creates a list where all the variables will be nested, which correspond to the term j.
            term_j= list()
            for i in range(len(Split_Pieces_in_Terms[j])):
                bb=Split_Pieces_in_Terms[j][i].split('.')
                for elem in bb:
                    term_j.append(elem)
            Split_Final.append(term_j)

    # This loop takes care of the signs in the string. If there is a - or a + will create entries of an array with those signs.

    for j,value in enumerate(Monster): # As we use enumerate (create pairs in the string), we need to add the value counter
        sub_string = Monster[j:1+j] # Piece to be read
        if sub_string == '-': # If there is a - in the previous sub_string, add - to the array
            Signs_match=np.append(Signs_match,"-")
        elif sub_string == '+': # Same as before, but now +
            Signs_match=np.append(Signs_match,"+")

    # Depending on the chosen number, it will spit specific chops.

    if number  == 0:
        return [Signs_match,Split_Terms]
    elif number == 1:
         return [Signs_match,Split_Pieces_in_Terms]
    elif number == 2:
         return [Signs_match,Split_Final]
    else:
         print("Wrong choice. Choose among 0,1,2")

# The following function is just to check that everything holds in the previous function. So we chop and reassamble to check that it makes sense.

def Checking_Right_Slipt(Terms_to_eat): # Function that checks that function Split Monster works fine, up to order 0.

    Final_Check = np.array([]) # The reasambled pieces here.
    Some_array_variables = Split_Monster(Terms_to_eat,0)[1] # Choose variables from previous chop function, up to (+,-) chop.
    Some_array_signs = Split_Monster(Terms_to_eat,0)[0] # Same with signs.

    for i in range(len(Some_array_variables)): #Append each previous pieces in the right order.
        Final_Check=np.append(Final_Check,(Some_array_signs[i],Some_array_variables[i]))

    Final_Check = ('').join(Final_Check) #Remove annoying spaces.

    if Final_Check == Terms_to_eat: #And let me know if the splitting was good.
         return print("Hurray, the program works")
    else:
         return print("Something went wrong. Double check!")
    
# This next function is in charge of eating two lists. The one we want to analyse and a reference one. If there is a sublist in the analysed one that resembles (but in any order) the reference one, that term (entry of the first list) will be chosen and spitted out.

def Looking_for_e(List_1, Reference):
    Chosen_ones = np.array([])
    
    Sequence_To_Inspect = Split_Monster(List_1,2)[1] # Split up to each variable.
    Sequence_To_Choose = Split_Monster(List_1,0)[1] # Split up to terms.

    for i in range(len(Sequence_To_Inspect)):
        for j,value in enumerate(Sequence_To_Inspect[i]): # As we use enumerate (create pairs in the string), we need to add the value counter. 
            sub_string = Sequence_To_Inspect[i][j:6+j] # Piece to be read
            sub_string.sort()
            if sub_string == Reference: # If the piece being read coincides with the reference one, add it to chosen ones.
                Chosen_ones = np.append(Chosen_ones,Sequence_To_Choose[i])

    return Chosen_ones

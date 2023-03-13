import numpy as np # importing numpy
from itertools import permutations

class Chop_Tools(object):
    """
    This class will allow us to chop and check that everything works by chopping and comparing. The only argument that eats is the monster (polynomial) to be chopped.

    It has several methods:

    Split_Monster, Check_Right_Split.
    """

    def __init__(self, Monster):
        self.Monster= Monster

    def Split_Monster(self, number): 
        
        """
        This function will eat the Monster as argument of the class and it will chop it into smaller lists depending on the selected number (the extra argument) as follows:

        number == 0, it will chop each term of the string and spit out signs in 1 array and terms in other.

        number == 1, it will chop further the terms and divide in multiplication.

        number == 2, it will go further and isolate each variable in each term.
        
        It also creates empty lists. Depending on the number you have chosen, it will one them fill it in and return it.
        """

        Split_Terms=np.array([]) # Empty array to split further those minuses
        Split_Pieces_in_Terms=list()
        Split_Final=list() # Empty array to split further those minuses
        Signs_match=np.array(['']) # Array whose 0th entry is a space, will go in front of first term of sequence.

        #Important to notice that I wrote self.Monster. This will look at the eaten argument in the class. No need to input it again.

        Split_First_Plus = self.Monster.split('+') # Split will separate previous string into only terms for each plus that reads through
        for i in range(len(Split_First_Plus)):# Loop that takes care of minuses
            Split_Terms=np.append(Split_Terms,Split_First_Plus[i].split('-'))
 
        for i in range(len(Split_Terms)): # Loop to split each term into the pieces separated by multiplication
            Split_Pieces_in_Terms.append(Split_Terms[i].split('*'))
    
        for j in range(len(Split_Pieces_in_Terms)): # These 2 loops are to split each piece into variables e_{i} and similar. It also creates a list where all the variables will be nested, which correspond to the term j.
            term_j= list()
            for i in range(len(Split_Pieces_in_Terms[j])):
                bb = Split_Pieces_in_Terms[j][i].split('.')
                for elem in bb:
                    term_j.append(elem)
            Split_Final.append(term_j)

        # This loop takes care of the signs in the string. If there is a - or a + will create entries of an array with those signs.

        for j,value in enumerate(self.Monster): # As we use enumerate (create pairs in the string), we need to add the value counter
            sub_string = self.Monster[j:1+j] # Piece to be read
            if sub_string == '-': # If there is a - in the previous sub_string, add - to the array
                Signs_match=np.append(Signs_match,"-")
            elif sub_string == '+': # Same as before, but now +
                Signs_match=np.append(Signs_match,"+")

        if number  == 0:
            return [Signs_match,Split_Terms]
        elif number == 1:
            return [Signs_match,Split_Pieces_in_Terms]
        elif number == 2:
            return [Signs_match,Split_Final]
        else:
            print("Wrong choice. Choose among 0,1,2")
    
    def Checking_Right_Slipt(self):
        """
        This function within the class is in charge of checking that our Split_Monster function chops in the right way. It will chop, assamble back and compare, spitting a hurray if everything went fine.
        """

        Final_Check = np.array([]) # The reasambled pieces here.
        Some_array_variables = self.Split_Monster(0)[1] # Choose variables from previous chop function, up to (+,-) chop.
        Some_array_signs = self.Split_Monster(0)[0] # Same with signs.

        for i in range(len(Some_array_variables)): #Append each previous pieces in the right order.
            Final_Check=np.append(Final_Check,(Some_array_signs[i],Some_array_variables[i]))

        Final_Check = ('').join(Final_Check) #Remove annoying spaces.

        if Final_Check == self.Monster: #And let me know if the splitting was good.
            return print("Hurray, the program works")
        else:
            return print("Something went wrong. Double check!")



        

        
import numpy as np # importing numpy
import time # To check how much time it takes to perform steps. We are dealing with plenty of objects
from itertools import permutations
from Functions_Amplitudes import * # Import function to be used
start_time = time.time() # Start clock

# To access my documents: cd ~/Library/Mobile\ Documents/com~apple~CloudDocs 

## Material to use and definitions

A123456 = np.loadtxt(fname="Loooong.csv", #Name of the file
 delimiter=",", #Object to look for in the file and separate as delimiter
 skiprows=0, # The amount of rows to not read
 dtype=str, # form of each of the entries
 )

Terms_to_play_with=''.join(A123456) # The to-be monster
#Terms_to_play_with = "e1.e2*e3.e6*e4.e5*ss1^-1*ss3*ss4^-1*ss6*tt3^-1- e1.e6*e2.e3*e4.e5*tt3^-1- k4.e3*k4.e5*e1.e6*e2.e4*ss1*ss3^-1*ss5^-1*tt2^-1- k4.e3*k4.e5*e1.e6*e2.e4*ss1*ss3^-1*ss6^-1*tt2^-1"
Ampl=Terms_to_play_with.replace("^-","$")
Amplitude=Ampl.replace(" ","")

Polarisation = ['e1', 'e2', 'e3', 'e4','e5','e6']

############################################################################

# Checking the chopping proccess

Checking_Right_Slipt(Amplitude)
Split_time= time.time()
print("Takes %s seconds to compare the assambled polynomial to initial one." % (time.time() - Split_time))

# Selecting the desired terms that will contribute to our malevoulus plan

Chosen_1_Iteration = Looking_for_e(Amplitude, Polarisation)
Split_time= time.time()
print("Takes %s seconds to chose our desired terms." % (time.time() - Split_time))

### TO DO: 
## Spit out terms in a .txt file
## SUBSTITION RULES. CAREFUL WITH SS TERMS AND TT.




##############################################################

## Material to try 

#animals = ['Hedhogdge','Chicken','Bird','Fish', 'Kroko', 'Dragon', 'Human']
#Only_you = ['Bird', 'Chicken']
#retrieved_elements = list(filter(lambda x: x in ll, animals))
#if retrieved_elements == animals:
 #       print("All are onboard")

#def Comparing(Test_List):
   
#    for j,value in enumerate(Test_List): # As we use enumerate (create pairs in the string), we need to add the value counter
#        sub_string = Test_List[j:2+j] # Piece to be read
 #       Only_you.sort()
  #      sub_string.sort()
   #     if sub_string == Only_you: # If there is a - in the previous sub_string, add - to the array
    #        print('Here they are')
     #   else:
      #      print('Nope')       
 

#Comparing(animals)




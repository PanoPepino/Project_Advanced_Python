import re
import Amplitude_Tools
from Amplitude_Tools import *


Str = '136452'

Perm = [*Str]
Momenta = ['s12','s23', 's34', 's45', 's56','s16']

Dict_Perm_Pol = {}
Dict_Perm_Mom = {}

for i in range(len(Perm)):
    Dict_Perm_Pol.update({Polarisation[i] : 'e' + str(Perm[i])})

for j in range(len(Momenta)):
    Entries = [Perm[j], Perm[(j+1) % len(Momenta)]]
    Entries.sort()
    Dict_Perm_Mom.update({Momenta[j] :'s' + str(Entries[0]) + str(Entries[1])})




print(Dict_Perm_Mom)
print(Dict_Perm_Pol)


print(Replacetor('Relevant_Terms.txt', Basic_Replacements)[2])

caca = 'e1.e2*e3.e5*e6.e4*s13*s12$1*(s13+s46-s25)$1'
aa=caca.split('*')

print(aa)








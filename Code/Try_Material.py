import re
import Amplitude_Tools
from Amplitude_Tools import *

List_To_Chose = [['e1.e3*e6.e4*e5.e2*s13$1*s46$1*s25$1*(s13-s46+s25)*(-s13+s46+s25)'],['e1.e2*e4.e3*e5.e6*s13$1*s46$1*s25$1*(s13-s46+s25)*(-s13+s46+s25)']]
List_To_Compare = [['e1', 'e3', 'e6', 'e4', 'e5', 'e2', 's13$1', 's46$1', 's25$1', '(s13-s46+s25)', '(-s13+s46+s25)'],['e1', 'e2', 'e4', 'e3', 'e5', 'e6', 's13$1', 's46$1', 's25$1', '(s13-s46+s25)', '(-s13+s46+s25)']]


To_write_down = list()
for i in range(len(List_To_Chose)):
    Chosen_ones_output= np.array([])
    for j in range(len(List_To_Compare[i][:3])):
        bb=List_To_Compare[i][2*j:2*j+2]
        bb.sort()
        Chosen_ones_output = np.append(Chosen_ones_output,bb)
        caca= Chosen_ones_output.ravel().tolist()
    
        if caca == ['e1', 'e2', 'e3', 'e4', 'e5', 'e6']:
            To_write_down.append(List_To_Chose[i])

print(To_write_down)
        


import numpy as np

def Read_Amplitude_Func(file):
    """
    This function eats the "name" (use "" and the name of file inside) of a .csv or .txt file and spits out a string that the system can interpret correctly.
    """

    Data= np.loadtxt(fname=file, #Name of the file
    delimiter=",", #Object to look for in the file and separate as delimiter
    skiprows=0, # The amount of rows to not read
    dtype=str, # form of each of the entries
    )

    Put_Terms_Togheter=''.join(Data) # The to-be monster
    Ampl_1=Put_Terms_Togheter.replace("^-","$")
    Amplitude=Ampl_1.replace(" ","")

    return Amplitude
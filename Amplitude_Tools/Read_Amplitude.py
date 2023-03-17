import numpy as np

def Read_Amplitude_Func(Name_file_extension):
    """
    This function eats file.csv or .txt file and spits out a string that the system can interpret correctly.
    """

    Amplitude= np.genfromtxt(Name_file_extension, dtype='str', delimiter=' ')


    return Amplitude


import Amplitude_Tools

Amplitude = Amplitude_Tools.Read_Amplitude_Func("Long.csv")

with open('Text.txt', 'w') as f:
    f.write(Amplitude)
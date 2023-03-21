import numpy as np


## Material to use and definitions

Basic_Replacements= { # Basic replacements of variables, to make easier connection with possible computations by hand.
    "ss1" : "s12",
    "ss2" : "s23",
    "ss3" : "s34",
    "ss4" : "s45",
    "ss5" : "s56",
    "ss6" : "s16",
    "tt1" : "(s12+s13+s23)",
    "tt2" : "(s23+s24+s34)",
    "tt3" : "(s34+s35+s45)",
  }

Extra_Replacements = { # To simplify even further. 
    "s46" : "s35",
    "s25" : "s16",
    "s65" : "s56", 
    "s43" : "s34", 
    "s45" : "s36",
    }

F_Replacements = {
    "F234" : "mZeta[2]*(ss4*ss5+ss1*ss6-ss4*tt1-ss1*tt3+tt1*tt3)",
    "F324" : "mZeta[2]*s13(ss2-ss6+tt3)",
    "F432" : "mZeta[2]*s14*s25",
    "F342" : "Zeta[2]*s13*s25",
    "F423" : "Zeta[2]*s14*s35",
    "F234" : "mZeta[2]*s35*(ss3-ss5+tt1)"
}

Polarisation = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6'] # The substring to look at
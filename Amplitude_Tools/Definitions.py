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

Extra_Replacements = { # To simplify even further. (Avoid first number to be even)
    "s46" : "s35",
    "s25" : "s16", 
    "s45" : "s36",
    "s24" : "s13",
    "s26" : "s15",
    "s23" : "s14",
    "mZeta[2]" : "(-1)*Zeta[2]"
    }

Sym_Replacements = { # To make always small number first. This can be coded. I have to think about it.
    "s65" : "s56",
    "s64" : "s46",
    "s63" : "s36",
    "s62" : "s26",
    "s61" : "s16",
    "s54" : "s45",
    "s53" : "s35",
    "s52" : "s25",
    "s51" : "s15",
    "s43" : "s34",
    "s42" : "s24",
    "s41" : "s14",
    "s32" : "s23",
    "s31" : "s13",
    "s21" : "s12",    
    }



Polarisation = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6'] # The substring to look at
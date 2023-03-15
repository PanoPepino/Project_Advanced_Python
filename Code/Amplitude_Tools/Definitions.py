import numpy as np


## Material to use and definitions

Basic_Replacements= {
    "ss1" : "s12",
    "ss2" : "s23",
    "ss3" : "s34",
    "ss4" : "s45",
    "ss5" : "s56",
    "ss6" : "s16",
    "tt1" : "(s12-s34+s56)",
    "tt2" : "(-s12+s34+s56)",
    "tt3" : "(s12+s34-s56)",
  }

Polarisation = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6'] # The substring to look at
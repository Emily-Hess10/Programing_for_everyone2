# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:56:20 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/poke1.csv")


vowels = ["A", "E", "I", "O", "U"]
poke_vowels_df = poke_df[poke_df["identifier"].str[0].str.upper().isin(vowels)]


poke_vowels_df.to_csv("q3.out", index=False)

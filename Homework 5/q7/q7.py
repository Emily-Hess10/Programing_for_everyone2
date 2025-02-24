# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:17:34 2025

@author: erhess
"""

import pandas as pd


df = pd.read_csv("../hw5_data/pokemon_species.csv")

mythical_legendary_df = df[(df["is_legendary"] != 0) | (df["is_mythical"] != 0)]


mythical_legendary_df.to_csv("q7.out", index=False)

print("Saved {len(mythical_legendary_df)} to q7.out")

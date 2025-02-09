# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:10:40 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/pokemon.csv")


def modify_pokemon_name(row):
    if row["height"] > 100:
        return row["identifier"].upper()  
    elif 50 <= row["height"] <= 60:
        return row["identifier"].title()  
    else:
        return row["identifier"].lower()  


poke_df["identifier"] = poke_df.apply(modify_pokemon_name, axis=1)


poke_df.to_csv("q7.out", index=False)

print("info has been written to q7")

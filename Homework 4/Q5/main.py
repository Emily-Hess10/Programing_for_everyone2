# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:07:24 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/poke1.csv")


prefix = input("Enter the letter for the Pokemon names: ")


filtered_poke_df = poke_df[poke_df["identifier"].str.startswith(prefix, na=False)]


if filtered_poke_df.empty:
    print(f"No Pokemon found starting with '{prefix}'.")
else:
    
    max_strength = filtered_poke_df["base_experience"].max()

    
    strongest_pokemon_df = filtered_poke_df[filtered_poke_df["base_experience"] == max_strength]

    
    strongest_pokemon_df = strongest_pokemon_df.sort_values(by="identifier", ascending=True)


    strongest_pokemon_df.to_csv("q5.out", index=False)

    print("written to q5.out.")

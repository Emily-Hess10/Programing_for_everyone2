# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:03:36 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/poke1.csv")

poke_p_df = poke_df[poke_df["identifier"].str.startswith("p", na=False)]


max_strength = poke_p_df["base_experience"].max()


strongest_pokemon_df = poke_p_df[poke_p_df["base_experience"] == max_strength]


strongest_pokemon_df = strongest_pokemon_df.sort_values(by="identifier", ascending=False)


strongest_pokemon_df.to_csv("q4.out", index=False)

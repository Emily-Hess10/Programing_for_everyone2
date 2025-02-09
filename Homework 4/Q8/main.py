# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:11:29 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/poke1.csv")
poke_types_df = pd.read_csv("../data/pokemon_types.csv")
types_df = pd.read_csv("../data/types.csv")


merged_df = pd.merge(poke_types_df, types_df, how="inner", left_on="type_id", right_on="id")


fire_type_pokemon = merged_df[merged_df["identifier"] == "fire"]


fire_pokemon_ids = fire_type_pokemon["pokemon_id"].unique()


remaining_pokemon_df = poke_df[~poke_df["id"].isin(fire_pokemon_ids)]


remaining_pokemon_count = remaining_pokemon_df.shape[0]


with open("q8.out", "w") as f:
    f.write(f"Number of remaining Pokemon: {remaining_pokemon_count}")


print(f"Number of remaining Pokemon: {remaining_pokemon_count}")

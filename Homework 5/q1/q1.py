# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:59:54 2025

@author: erhess
"""


import pandas as pd


pokemon_species = pd.read_csv("../hw5_data/pokemon_species.csv")
generations = pd.read_csv("../hw5_data/generations.csv")


pokemon_species.columns = pokemon_species.columns.str.strip()
generations.columns = generations.columns.str.strip()


pokemon_species["generation_id"] = pokemon_species["generation_id"].astype(int)
generations["id"] = pd.to_numeric(generations["id"], errors="coerce").dropna().astype(int)


merged_df = pokemon_species.merge(generations, left_on="generation_id", right_on="id", suffixes=("_species", "_gen"))
merged_df.to_csv("q1.out", index=False)


result_df = merged_df[["identifier_species", "identifier_gen"]]  
result_df.columns = ["pokemon_name", "generation_name"]


result_df.to_csv("q1.csv", index=False)

print("Files q1.ouyt and q1.csv have been saved.")

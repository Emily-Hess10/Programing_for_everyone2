# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:16:26 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/poke1.csv")


special_pokemon = poke_df[poke_df["identifier"].str.contains("-")]


special_pokemon["cleaned_name"] = special_pokemon["identifier"].str.replace("-", "", regex=False)


unique_cleaned_names = special_pokemon["cleaned_name"].drop_duplicates()


unique_cleaned_names.to_csv("q11.out")


print(unique_cleaned_names)

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:13:55 2025

@author: erhess
"""

import pandas as pd


types = pd.read_csv("../hw5_data/types.csv")
pokemon_types = pd.read_csv("../hw5_data/pokemon_types.csv")


types.columns = types.columns.str.strip()
pokemon_types.columns = pokemon_types.columns.str.strip()


secondary_types = pokemon_types[pokemon_types["slot"] == 2]


type_counts = secondary_types["type_id"].value_counts().reset_index()
type_counts.columns = ["type_id", "count"]


type_counts = type_counts.merge(types, left_on="type_id", right_on="id", suffixes=("_count", "_type"))


final_counts = type_counts[["identifier", "count"]]


output_path = "q6.out"
final_counts.to_csv(output_path, index=False)

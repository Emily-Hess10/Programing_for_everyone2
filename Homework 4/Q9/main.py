# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:13:58 2025

@author: erhess
"""

import pandas as pd

poke_df = pd.read_csv("../data/poke1.csv")
encounters_df = pd.read_csv("../data/encounters.csv")
location_area_df = pd.read_csv("../data/location_areas.csv")
locations_df = pd.read_csv("../data/locations.csv")


merged_df = pd.merge(encounters_df, location_area_df, how="inner", left_on="location_area_id", right_on="id")
merged_df = pd.merge(merged_df, locations_df, how="inner", left_on="location_id", right_on="id")


location_pokemon_count = merged_df.groupby("region_id")["id"].nunique().reset_index()


sorted_location_pokemon_count = location_pokemon_count.sort_values(by="id", ascending=False)

top_5_locations = sorted_location_pokemon_count.head(5)

top_5_locations.to_csv('q9.out', index=False)


print(top_5_locations)

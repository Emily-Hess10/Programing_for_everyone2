# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:15:31 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/poke1.csv")
encounters_df = pd.read_csv("../data/encounters.csv")
location_area_df = pd.read_csv("../data/location_areas.csv")
locations_df = pd.read_csv("../data/locations.csv")


location_area_df = location_area_df.rename(columns={"id": "location_area_id"})
locations_df = locations_df.rename(columns={"id": "location_id"})
poke_df = poke_df.rename(columns={"id": "pokemon_id"})


merged_df = pd.merge(encounters_df, location_area_df, how="inner", on="location_area_id")
merged_df = pd.merge(merged_df, locations_df, how="inner", on="location_id")


merged_df = pd.merge(merged_df, poke_df, how="inner", on="pokemon_id")


pokemon_location_counts = merged_df.groupby("identifier")["location_id"].nunique().reset_index()


pokemon_location_counts = pokemon_location_counts.rename(columns={"location_id": "num_locations"})


most_locations = pokemon_location_counts[pokemon_location_counts["num_locations"] == pokemon_location_counts["num_locations"].max()]
fewest_locations = pokemon_location_counts[pokemon_location_counts["num_locations"] == pokemon_location_counts["num_locations"].min()]


result_df = pd.concat([most_locations, fewest_locations])


result_df.to_csv("q10.out")


print(result_df)

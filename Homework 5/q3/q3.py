# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:07:58 2025

@author: erhess
"""

import pandas as pd
import matplotlib.pyplot as plt


pokemon_species = pd.read_csv("../hw5_data/pokemon_species.csv")
regions = pd.read_csv("../hw5_data/regions.csv")


pokemon_species.columns = pokemon_species.columns.str.strip()
regions.columns = regions.columns.str.strip()


merged_df = pokemon_species.merge(regions, left_on="generation_id", right_on="id", suffixes=("_species", "_region"))

region_counts = merged_df["identifier_region"].value_counts().reset_index()
region_counts.columns = ["identifier", "pokemon_count"]


region_counts["identifier"] = region_counts["identifier"].str.capitalize()


plt.figure(figsize=(10, 6))
plt.bar(region_counts["identifier"], region_counts["pokemon_count"], color="royalblue")

plt.xlabel("Region (Identifier)", fontsize=12)
plt.ylabel("Number of Pokémon", fontsize=12)
plt.title("Number of Pokémon per Region", fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)


plt.tight_layout()
plt.show()

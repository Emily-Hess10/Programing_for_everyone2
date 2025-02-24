# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:18:45 2025

@author: erhess
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../hw5_data/pokemon_species.csv")
pokemon = pd.read_csv("../hw5_data/pokemon.csv")


legendary_mythical = df[(df['is_legendary'] == 1) | (df['is_mythical'] == 1)]


legendary_mythical = legendary_mythical[['id', 'identifier']] 
pokemon = pokemon[['id', 'identifier', 'base_experience', 'height', 'weight']] 


merged = legendary_mythical.merge(pokemon, on="id", suffixes=("_species", "_main"))


merged["Strength"] = (merged["base_experience"] * 5) + ((merged["height"] + merged["weight"]) * 5)

top5 = merged.nlargest(5, "Strength")


top5.to_csv("q8.out", index=False)


plt.figure(figsize=(10, 5))
plt.bar(top5["identifier_main"], top5["Strength"], color="purple")
plt.xlabel("Pokémon")
plt.ylabel("Strength")
plt.title("Top 5 Strongest Legendary & Mythical Pokémon")
plt.xticks(rotation=45)
plt.show()


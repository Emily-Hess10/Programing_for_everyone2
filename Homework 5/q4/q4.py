# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:12:31 2025

@author: erhess
"""
import pandas as pd
import matplotlib.pyplot as plt
import random


pokemon = pd.read_csv("../hw5_data/pokemon.csv")
df_species = pd.read_csv("../hw5_data/pokemon_species.csv")
df_colors = pd.read_csv("../hw5_data/pokemon_colors.csv")


merged_species_color = pd.merge(df_species[['id', 'color_id']], pokemon[['id', 'identifier', 'base_experience']], on='id')


merged = pd.merge(merged_species_color, df_colors[['id', 'identifier']], left_on='color_id', right_on='id', suffixes=('_species', '_color'))


pokemon_with_color = merged[['identifier_species', 'base_experience', 'identifier_color']].rename(columns={'identifier_species': 'pokemon_name', 'identifier_color': 'primary_color'})

pokemon_with_color.to_csv("q4.out", index=False)


random_pokemon = pokemon_with_color.sample(10)


plt.figure(figsize=(10, 6))
bars = plt.bar(random_pokemon['pokemon_name'], random_pokemon['base_experience'], color=random_pokemon['primary_color'])

# Add labels and title
plt.xlabel("Pokémon")
plt.ylabel("Base Experience")
plt.title("Base Experience of 10 Random Pokémon with Their Primary Colors")


plt.xticks(rotation=45)


plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:13:43 2025

@author: erhess
"""

import pandas as pd
import matplotlib.pyplot as plt


pokemon_types = pd.read_csv("../hw5_data/pokemon_types.csv")
types = pd.read_csv("../hw5_data/types.csv")


merged_df = pokemon_types.merge(types, left_on='type_id', right_on='id', suffixes=('_pokemon', '_type'))


type_counts = merged_df["identifier"].value_counts().reset_index()
type_counts.columns = ["type", "count"]


def assign_color(type_name):
    color_map = {
        'Fire': 'red', 'Water': 'blue', 'Grass': 'green', 'Electric': 'yellow', 'Psychic': 'purple',
        'Ice': 'cyan', 'Dragon': 'orange', 'Dark': 'black', 'Fairy': 'pink', 'Fighting': 'brown',
        'Rock': 'gray', 'Ground': 'sienna', 'Poison': 'violet', 'Flying': 'skyblue',
        'Bug': 'lime', 'Ghost': 'indigo', 'Steel': 'silver', 'Normal': 'beige'
    }
    return color_map.get(type_name, 'gray')


type_counts['type_color'] = type_counts['type'].apply(assign_color)


type_counts.to_csv("q5.out", index=False)


plt.figure(figsize=(12, 6))
bars = plt.bar(type_counts['type'], type_counts['count'], color=type_counts['type_color'])

plt.xlabel("Pokemon Type")
plt.ylabel("Number of Pokemon")
plt.title("Number of Pokemon by Primary Type")
plt.xticks(rotation=45)

plt.show()

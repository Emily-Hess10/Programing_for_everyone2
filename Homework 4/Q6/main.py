# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:09:19 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/pokemon.csv")           
poke_types_df = pd.read_csv("../data/pokemon_types.csv")  
types_df = pd.read_csv("../data/types.csv")         


pokemon_name = input("Enter a Pokemon name: ").lower()


pokemon_exists = poke_df[poke_df["identifier"].str.lower() == pokemon_name]

if pokemon_exists.empty:
    print("pokemon does not exist")
else:
    
    pokemon_id = pokemon_exists.iloc[0]["id"]
    
    
    pokemon_types = pd.merge(poke_types_df[poke_types_df["identifier"] == pokemon_id],
                             types_df, left_on="identifier", right_on="id", how='left')
    
    
    pokemon_type_list = pokemon_types["identifier"].tolist()
    
  
    print(f"{pokemon_name.capitalize()} is of type(s): {', '.join(pokemon_type_list)}")
    
    
    all_pokemon_of_type = poke_types_df[poke_types_df['type_id'].isin(pokemon_types['type_id'])]
    
   
    all_pokemon_of_type_df = pd.merge(all_pokemon_of_type, poke_df, left_on='poke_id', right_on='id', how='left')
    
  
    type_count = all_pokemon_of_type_df['name'].nunique()
    print(f"Total number of Pokémon of these types: {type_count}")
    
    
    strongest_pokemon = all_pokemon_of_type_df.loc[all_pokemon_of_type_df['strength'].idxmax()]
    weakest_pokemon = all_pokemon_of_type_df.loc[all_pokemon_of_type_df['strength'].idxmin()]
    
    print(f"The strongest Pokémon of this type is: {strongest_pokemon['name']} with strength {strongest_pokemon['strength']}")
    print(f"The weakest Pokémon of this type is: {weakest_pokemon['name']} with strength {weakest_pokemon['strength']}")
    
    
    output = {
        "pokemon_name": pokemon_name,
        "types": pokemon_type_list,
        "total_count": type_count,
        "strongest_pokemon": strongest_pokemon['name'],
        "strongest_strength": strongest_pokemon['strength'],
        "weakest_pokemon": weakest_pokemon['name'],
        "weakest_strength": weakest_pokemon['strength']
    }
    
    #
    with open('q5.out', 'w') as f:
        f.write(f"Pokémon: {output['pokemon_name']}")
        f.write(f"Types: {', '.join(output['types'])}")
        f.write(f"Total count of Pokémon of this type: {output['total_count']}")
        f.write(f"Strongest Pokémon: {output['strongest_pokemon']} (Strength: {output['strongest_strength']})")
        f.write(f"Weakest Pokémon: {output['weakest_pokemon']} (Strength: {output['weakest_strength']})")
    
    print("Results written to q5.out.")

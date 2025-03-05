# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 15:35:11 2025

@author: erhess
"""

#fixed errors in this homework 

import pandas as pd


poke_df = pd.read_csv("../data/pokemon.csv")           
poke_types_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/EC1/data/pokemon_types.csv")  
types_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/EC1/data/types.csv")          

pokemon_name = input("Enter a Pokemon name: ").strip().lower()


pokemon_exists = poke_df[poke_df["identifier"].str.lower() == pokemon_name]

if pokemon_exists.empty:
    print("Pokemon does not exist.")
else:
    pokemon_id = pokemon_exists.iloc[0]["id"]
    
    
    pokemon_types = poke_types_df[poke_types_df["pokemon_id"] == pokemon_id].merge(
        types_df, left_on="type_id", right_on="id", how="left"
    )

  
    if "identifier" in types_df.columns:
        pokemon_type_list = pokemon_types["identifier"].tolist()  
    else:
        print("Error: `types_df` does not contain an `identifier` column.")
        pokemon_type_list = []

    print(f"{pokemon_name.capitalize()} is of type(s): {', '.join(pokemon_type_list)}")

    
    all_pokemon_of_type = poke_types_df[poke_types_df['type_id'].isin(pokemon_types['type_id'])]

    
    all_pokemon_of_type_df = all_pokemon_of_type.merge(
        poke_df, left_on='pokemon_id', right_on='id', how='left'
    )

    type_count = all_pokemon_of_type_df['identifier'].nunique()
    print(f"Total number of Pokemon of these types: {type_count}")

    
    if 'base_experience' in all_pokemon_of_type_df.columns:
        strongest_pokemon = all_pokemon_of_type_df.loc[all_pokemon_of_type_df['base_experience'].idxmax()]
        weakest_pokemon = all_pokemon_of_type_df.loc[all_pokemon_of_type_df['base_experience'].idxmin()]

        print(f"The strongest Pokemon of this type is: {strongest_pokemon['identifier']} with base experience {strongest_pokemon['base_experience']}")
        print(f"The weakest Pokemon of this type is: {weakest_pokemon['identifier']} with base experience {weakest_pokemon['base_experience']}")

        
        with open('q5.out', 'w') as f:
            f.write(f"Pokemon: {pokemon_name.capitalize()}\n")
            f.write(f"Types: {', '.join(pokemon_type_list)}\n")
            f.write(f"Total count of Pokemon of this type: {type_count}\n")
            f.write(f"Strongest Pokemon: {strongest_pokemon['identifier']} (Base Experience: {strongest_pokemon['base_experience']})\n")
            f.write(f"Weakest Pokemon: {weakest_pokemon['identifier']} (Base Experience: {weakest_pokemon['base_experience']})\n")

        print("Results written to q5.out.")
    else:
        print("Base experience data is missing. Cannot determine strongest/weakest Pokémon.")


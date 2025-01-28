# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:57:18 2025

@author: erhess
"""

#Q7 Homework 1
import pandas as pd

def search_pokemon(df, pokemon_name):
    
    pokemon_name = pokemon_name.strip().lower()

    
    result = df[df['identifier'].str.lower() == pokemon_name]

    
    if not result.empty:
        return result['id'].values[0], result['identifier'].values[0]  

def main():
    
    df = pd.read_csv('C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 1/poke (1).csv') 

    
    team = []

    print("Welcome to the team builder!")
    print("You can add up to 6 pokemon to your team. write exit to exit.")
    
    while len(team) < 6:
        pokemon_name = input(f"Enter the name of Pokémon {len(team)+1} (or type 'exit' to finish): ").strip()

        if pokemon_name.lower() == 'exit':
            break

       
        result = search_pokemon(df, pokemon_name)

        if result:
            poke_id, poke_name = result
            team.append((poke_id, poke_name))
            print(f"Added {poke_name}  to your team.")
        else:
            print("Pokemon does not exist in the dataset.")

    
    if team:
        with open('q7.out', 'w') as output_file:
            for poke_id, poke_name in team:
                output_file.write(f"ID: {poke_id}, Name: {poke_name}")
        print("Your team has been saved to q7.out.")
        print(team)
    else:
        print("No Pokemon were added to the team.")

if __name__ == "__main__":
    main()

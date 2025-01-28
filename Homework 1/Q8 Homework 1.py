# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:29:00 2025

@author: erhess
"""

#Q8 Homework 1

import pandas as pd

def search_pokemon(df, pokemon_name):
    
    pokemon_name = pokemon_name.strip().lower()

    
    result = df[df['identifier'].str.lower() == pokemon_name]

    
    if not result.empty:
        return result['id'].values[0], result['identifier'].values[0]  
    return None

def get_pokemon_locations(location_area_id_df, pokemon_id):
    
    locations = location_area_id_df[location_area_id_df['pokemon_id'] == pokemon_id]

    
    return locations['location'].tolist()

def main():
    
    df = pd.read_csv('C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 1/poke (1).csv')  
    locations_df = pd.read_csv('C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 1/locations (1).csv') 

   
    team = []
    pokemon_locations = {}

    print("Welcome to the Pokémon team builder with locations")
    print("You can add up to 6 Pokémon to your team. Type exit to exit.")
    
    while len(team) < 6:
        pokemon_name = input(f"Enter the name of Pokémon {len(team)+1} (or type 'exit' to finish): ").strip()

        if pokemon_name.lower() == 'exit':
            break

        
        result = search_pokemon(df, pokemon_name)

        if result:
            poke_id, poke_name = result
           
            locations = get_pokemon_locations(locations_df, poke_id)
            
            
            team.append((poke_id, poke_name))
            pokemon_locations[poke_id] = locations

            print(f"Added {poke_name} (ID: {poke_id}) to your team. Locations: {', '}")
        else:
            print("Pokemon does not exist in the dataset.")

   
    if team:
        with open('q8.out', 'w') as output_file:
            for poke_id, poke_name in team:
                
                locations = ', '.join(pokemon_locations[poke_id])
                output_file.write(f"ID: {poke_id}, Name: {poke_name}, Locations: {locations}")
        print("Your team and locations have been saved to q8.out.")
    else:
        print("No Pokémon were added to the team.")

if __name__ == "__main__":
    main()

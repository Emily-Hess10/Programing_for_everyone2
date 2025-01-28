# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:48:01 2025

@author: erhess
"""

#Q9 Homework 1
import pandas as pd

def search_pokemon(df, pokemon_name):
    
    pokemon_name_lower = pokemon_name.strip().lower()

    
    result = df[df['identifier'].str.lower() == pokemon_name_lower]

    
    if not result.empty:
        return result['id'].values[0], result['identifier'].values[0]  
    return None

def get_pokemon_locations(locations_df, pokemon_id):
    
    locations = locations_df[locations_df['pokemon_id'] == pokemon_id]

    
    return locations['location'].tolist()

def display_team(team):
    
    if team:
        print("Your team:")
        for idx, (poke_id, poke_name) in enumerate(team, start=1):
            print(f"{idx}) {poke_name} (ID: {poke_id})")
    else:
        print("Your team is currently empty.")

def opening():
    print("Welcome to the Pokemon team ")
    print("""
          What would you like to do? 
          1. Add Pokémon
          2. List Team
          3. Drop Member
          4. Exit
    """)

def main():
    
    df = pd.read_csv('poke.csv')  
    locations_df = pd.read_csv('locations.csv')  # 
   
    team = []
    pokemon_locations = {}

    while True:
        opening()
        try:
            action = int(input("Choose an action: "))
        except ValueError:
            print("Please choose a valid number from the list.")
            continue 

        if action == 1:
            
            pokemon_name = input("Enter the name of the Pokémon to add: ").strip()

            
            result = search_pokemon(df, pokemon_name)

            if result:
                poke_id, poke_name = result
                
                locations = get_pokemon_locations(locations_df, poke_id)
                
                
                team.append((poke_id, poke_name))
                pokemon_locations[poke_id] = locations
                print(f"Added {poke_name} (ID: {poke_id}) to your team. Locations: {', '.join(locations)}")
            else:
                print("Pokemon does not exist in the dataset.")

        elif action == 2:
            
            display_team(team)

        elif action == 3:
            
            if not team:
                print("Your team is empty. No Pokemon to remove.")
            else:
                display_team(team)
                try:
                    pokemon_id_to_remove = int(input("Enter the ID of the Pokémon to remove: "))
                    
                    team = [member for member in team if member[0] != pokemon_id_to_remove]
                    print(f"Pokémon with ID {pokemon_id_to_remove} has been removed from the team.")
                except ValueError:
                    print("Invalid ID. Please enter a valid number.")

        elif action == 4:
            
            if team:
                with open('q9.out', 'w') as output_file:
                    for poke_id, poke_name in team:
                        locations = ', '.join(pokemon_locations[poke_id])
                        output_file.write(f"ID: {poke_id}, Name: {poke_name}, Locations: {locations}\n")
                print("Your team and locations have been saved to q9.out.")
            else:
                print("No Pokemon to save.")
            break  

        else:
            print("Please choose a valid number from the list.")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:03:53 2025

@author: erhess
"""

import pandas as pd


def search_pokemon(df, pokemon_name):
    pokemon_name = pokemon_name.strip().lower()
    result = df[df['identifier'].str.lower() == pokemon_name]
    if not result.empty:
        return result['id'].values[0], result['identifier'].values[0]  
    return None


def main():
    
    df = pd.read_csv('C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 1/poke (1).csv')  

    
    team = []

    print("Welcome to the Pokemon team builder")
    print("You can add up to 6 Pokémon to your team.")
    
    while True:
        print("a. Add To Team")
        print("b. Drop From Team")
        print("c. Print Team")
        print("d. Exit")
        
        choice = input("What would you like to do? ").strip().lower()

        if choice == 'a':  
            if len(team) >= 6:
                print("Too many team members.")
                continue  
            
            pokemon_name = input("Enter the name of the Pokemon to add: ").strip()
            result = search_pokemon(df, pokemon_name)

            if result:
                poke_id, poke_name = result
                team.append((poke_id, poke_name))
                print(f"Added {poke_name} (ID: {poke_id}) to your team.")
            else:
                print("This Pokémon does not exist.")

        elif choice == 'b':  
            if not team:
                print("Your team is empty.")
                continue  
            
            print("Current team:")
            for idx, (poke_id, poke_name) in enumerate(team, 1):
                print(f"{idx}. {poke_name} (ID: {poke_id})")
            
            drop_choice = input("Enter the number of the Pokémon to drop: ").strip()
            try:
                drop_idx = int(drop_choice) - 1
                if 0 <= drop_idx < len(team):
                    dropped_pokemon = team.pop(drop_idx)
                    print(f"Dropped {dropped_pokemon[1]} from the team.")
                else:
                    print("Invalid selection. No Pokémon was dropped.")
            except ValueError:
                print("Please provide a valid number.")

        elif choice == 'c':  
            if not team:
                print("Your team is empty.")
            else:
                print("Your current team:")
                team_df = pd.DataFrame(team, columns=['ID', 'Name'])
                print(team_df)

        elif choice == 'd':  
            print("Exiting the team builder.")
            break
        
        else:
            print("pick a, b, c, or d.")

if __name__ == "__main__":
    main()

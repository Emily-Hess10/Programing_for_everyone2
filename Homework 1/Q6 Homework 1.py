# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:28:58 2025

@author: erhess
"""

#Q6 Homework 1 

import pandas as pd

def search_pokemon(df, pokemon_name):
    
    pokemon_name_lower = pokemon_name.strip().lower()

    
    result = df[df['identifier'].str.lower() == pokemon_name_lower]
    
    
    if not result.empty:
        return result['id'].values[0], result['identifier'].values[0]  
    return None

def main():
    
    df = pd.read_csv('C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 1/poke (1).csv')
    
    
    pokemon_name = input("Enter the name of the pokemon: ")
# I forget hpw to upload a cvs not on my one drive
    
    result = search_pokemon(df, pokemon_name)
    
    
    if result:
        poke_id, poke_name = result
        with open('q6.out', 'w') as output_file:
            output_file.write(f"ID: {poke_id}, Name: {poke_name}\n")
        print(f"Pokemon found and has been written to q6.out.")
    else:
        print("Pokemon does not exist.")

if __name__ == "__main__":
    main()

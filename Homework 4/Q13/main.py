# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:20:27 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("../data/poke1.csv")

def save_to_file():
    poke_df.to_csv("q13.out", index=False)
    print("saved to q13.out")

def add_pokemon():
    print("Adding a new Pokemon:")
    new_id = int(input("Enter Pokemon id: "))
    new_name = input("Enter Pokemon name: ")
    new_height = float(input("Enter Pokemon height: "))
    new_weight = float(input("Enter Pokemon weight: "))

    poke_df.loc[len(poke_df)] = [new_id, new_name, new_height, new_weight]
    print(f"Pokemon {new_name} added")

def delete_pokemon():
    pokemon_id = int(input("Enter Pokemon id: "))
    
    if pokemon_id in poke_df["id"].values:
        poke_df.drop(poke_df[poke_df["id"] == pokemon_id].index, inplace=True)
        print(f"Pokemon with {pokemon_id} deleted")
    else:
        print("Pokémon with this ID does not exist.")

def update_pokemon():
    pokemon_id = int(input("Enter Pokemon id: "))
    
    
    if pokemon_id in poke_df["id"].values:
        new_name = input("Enter new Pokemon name: ")
        poke_df.loc[poke_df["id"] == pokemon_id, "name"] = new_name
        print(f"Pokemon id {pokemon_id} updated to {new_name}.")
    else:
        print("Pokemon with this idD does not exist")

def manage_dataset():
    while True:
        print("Manage Dataset:")
        print("1. Add Pokemon")
        print("2. Delete Pokemon")
        print("3. Update Pokemon")
        print("4. Go back to main menu")

    
        choice = input("Enter your choice: ")

        if choice == "1":
            add_pokemon()
        elif choice == "2":
            delete_pokemon()
        elif choice == "3":
            update_pokemon()
        elif choice == "4":
            break
        else:
            print("error")

def main_menu():
    while True:
        print("Main Menu:")
        print("a. Manage Dataset")
        print("b. Exit")

       
        choice = input("Enter your choice: ").lower()

        if choice == "a":
            manage_dataset()
        elif choice == "b":
            save_to_file()
            break
        else:
            print("Invalid choice. Please try again.")


main_menu()

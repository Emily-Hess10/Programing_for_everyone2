# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 15:45:41 2025

@author: erhess
"""

import pandas as pd

# Load dataset
poke_df = pd.read_csv("../data/poke1.csv")

def save_to_file():
    poke_df.to_csv("q13.out", index=False)
    print("Saved to q13.out")

def add_pokemon():
    print("Adding a new Pokémon:")
    new_id = int(input("Enter Pokémon ID: "))
    new_name = input("Enter Pokémon name: ")
    new_height = float(input("Enter Pokémon height: "))
    new_weight = float(input("Enter Pokémon weight: "))

    # Ensure all required columns are included
    new_data = pd.DataFrame([{
        "id": new_id,
        "identifier": new_name,  # Assuming "identifier" is the correct column for names
        "height": new_height,
        "weight": new_weight
    }])

    global poke_df  # Ensure modifications persist
    poke_df = pd.concat([poke_df, new_data], ignore_index=True)

    print(f"Pokémon {new_name} added.")

def delete_pokemon():
    pokemon_id = int(input("Enter Pokémon ID: "))

    global poke_df  # Ensure modifications persist
    if pokemon_id in poke_df["id"].values:
        poke_df = poke_df[poke_df["id"] != pokemon_id]  # Remove the row properly
        print(f"Pokémon with ID {pokemon_id} deleted.")
    else:
        print("Pokémon with this ID does not exist.")

def update_pokemon():
    pokemon_id = int(input("Enter Pokémon ID: "))

    if pokemon_id in poke_df["id"].values:
        new_name = input("Enter new Pokémon name: ")
        poke_df.loc[poke_df["id"] == pokemon_id, "identifier"] = new_name  # Corrected column name
        print(f"Pokémon ID {pokemon_id} updated to {new_name}.")
    else:
        print("Pokémon with this ID does not exist.")

def manage_dataset():
    while True:
        print("\nManage Dataset:")
        print("1. Add Pokémon")
        print("2. Delete Pokémon")
        print("3. Update Pokémon")
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
            print("Error: Invalid choice.")

def main_menu():
    while True:
        print("\nMain Menu:")
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

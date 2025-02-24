# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:04:48 2025

@author: erhess
"""

import pandas as pd
import random


poke_df = pd.read_csv("../hw5_data/pokemon.csv")


pokemon_team = []

def save_team():
    """Save the current Pokemon team to a file."""
    team_df = pd.DataFrame(pokemon_team, columns=["id", "name", "height", "weight"])
    team_df.to_csv("pokemon_team.out", index=False)
    print("Team saved to pokemon_team.out")

def add_pokemon():
    """Add a Pokeon to the team if it exists in the dataset and the team is not fill."""
    if len(pokemon_team) >= 6:
        print("Your team already has 6 Pokemon. Remove one.")
        return

    pokemon_name = input("Enter the Pokemon name: ").strip().lower()
    found_pokemon = poke_df[poke_df["name"].str.lower() == pokemon_name]

    if not found_pokemon.empty:
        pokemon_team.append(found_pokemon.iloc[0].tolist())
        print("{pokemon_name.capitalize()} added to your team")
    else:
        print("Pokemon not found in the dataset.")

def generate_random_team():
    """getting random team of 6 Pokemon from the dataset."""
    global pokemon_team
    pokemon_team = poke_df.sample(n=6).values.tolist()
    print("Random Pokemon team generated!")

def delete_pokemon():
    """Remove a Pokémon from the team."""
    pokemon_name = input("Enter the Pokemon name to remove: ").strip().lower()
    for pokemon in pokemon_team:
        if pokemon[1].lower() == pokemon_name:
            pokemon_team.remove(pokemon)
            print(f"{pokemon_name.capitalize()} removed from your team!")
            return
    print("Pokemon not found")

def manage_team():
    """Display the team management menu."""
    while True:
        print("\nManage Pokemon Team:")
        print("1. Add Pokemon")
        print("2. Generate Random Team")
        print("3. Delete Pokemon")
        print("4. Go back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_pokemon()
        elif choice == "2":
            generate_random_team()
        elif choice == "3":
            delete_pokemon()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def main_menu():
    """Display the main menu."""
    while True:
        print("Main Menu:")
        print("a. Manage Team")
        print("b. Exit")

        choice = input("Enter your choice: ").lower()

        if choice == "a":
            manage_team()
        elif choice == "b":
            save_team()
            break
        else:
            print("Invalid choice")

main_menu()

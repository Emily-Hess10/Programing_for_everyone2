# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:19:42 2025

@author: erhess
"""

import pandas as pd
import random


df = pd.read_csv("../hw5_data/pokemon.csv")

dungeon_size = 4
dungeon = [[None for _ in range(dungeon_size)] for _ in range(dungeon_size)]


exit_x, exit_y = random.randint(0, 3), random.randint(0, 3)
start_x, start_y = random.randint(0, 3), random.randint(0, 3)


while (exit_x, exit_y) == (start_x, start_y):
    exit_x, exit_y = random.randint(0, 3), random.randint(0, 3)


available_pokemon = df.sample(n=14).to_dict(orient="records")  
index = 0

for i in range(dungeon_size):
    for j in range(dungeon_size):
        if (i, j) != (start_x, start_y) and (i, j) != (exit_x, exit_y):
            dungeon[i][j] = available_pokemon[index]
            index += 1


user_choice = input("Would you like to (1) build a team or (2) randomly generate one? ")

if user_choice == "1":
    print("Choose up to 6 Pokémon from the list:")
    print(df.sample(20)[["Name", "base_experience"]])  
    team = []
    while len(team) < 6:
        choice = input("Enter Pokemon name (or type 'done' to finish): ").strip()
        if choice.lower() == "done":
            break
        pokemon = df[df["Name"].str.lower() == choice.lower()]
        if not pokemon.empty:
            team.append(pokemon.iloc[0].to_dict())
            print(f"{choice} added to your team!")
        else:
            print("Invalid Pokémon name. Try again.")
else:
    team = df.sample(n=6).to_dict(orient="records")
    print("Your randomly generated team:")
    for p in team:
        print(f"{p['Name']} (Base XP: {p['base_experience']})")


x, y = start_x, start_y
while True:
    print(f"\nYou are currently at position ({x+1}, {y+1}) in the dungeon.")

    move = input("Move (WASD), 'exit' to quit: ").lower()

    if move == "exit":
        with open("status.out", "w") as f:
            f.write("Failure\n")
        print("You exited the dungeon. Game Over.")
        break

   
    new_x, new_y = x, y
    if move == "w" and x > 0:
        new_x -= 1
    elif move == "s" and x < dungeon_size - 1:
        new_x += 1
    elif move == "a" and y > 0:
        new_y -= 1
    elif move == "d" and y < dungeon_size - 1:
        new_y += 1
    else:
        print("Invalid move")
        continue

   
    if (new_x, new_y) == (exit_x, exit_y):
        with open("status.out", "w") as f:
            f.write(" {len(team)} members remaining\n")
        print(f"🎉 You found the exit with {len(team)} Pokemon ")
        break

    
    encountered_pokemon = dungeon[new_x][new_y]
    if encountered_pokemon:
        print("You encountered {encountered_pokemon['Name']} (Base XP: {encountered_pokemon['base_experience']})!")

        
        if team:
            player_pokemon = team[0]  
            print("Your {player_pokemon['Name']} is fighting")

            if player_pokemon["base_experience"] >= encountered_pokemon["base_experience"]:
                print("You defeated {encountered_pokemon['Name']} and continue forward!")
                dungeon[new_x][new_y] = None  
            else:
                print("{player_pokemon['Name']} was defeated and removed")
                team.pop(0)  

                if not team:
                    with open("status.out", "w") as f:
                        f.write("Failure\n")
                    print("You have no Pokemon left Game Over.")
                    break
    x, y = new_x, new_y

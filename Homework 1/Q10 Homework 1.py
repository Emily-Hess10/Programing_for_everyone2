# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:52:10 2025

@author: erhess
"""

#Q10 Homework 1
import random


row = 2
colums = 4

def create_dungeon():
    
    start_pos = (random.randint(0, row-1), random.randint(0, colums-1))
    exit_pos = (random.randint(0, row-1), random.randint(0, colums-1))
    

    while start_pos == exit_pos:
        exit_pos = (random.randint(0, row-1), random.randint(0, colums-1))
    
    return start_pos, exit_pos

def display_dungeon(player_pos, exit_pos):
    
    for r in range(row):
        for c in range(colums):
            if (r, c) == player_pos:
                print("P", end=" ")            
            elif (r, c) == exit_pos:

                print("E", end=" ")
            else:
                print(".", end=" ")
        print()  

def is_valid_move(pos):
    
    return 0 <= pos[0] < row and 0 <= pos[1] < colums

def move_player(player_pos, direction):
    
    if direction == "up":
        new_pos = (player_pos[0] - 1, player_pos[1])
    elif direction == "down":
        new_pos = (player_pos[0] + 1, player_pos[1])
    elif direction == "left":
        new_pos = (player_pos[0], player_pos[1] - 1)
    elif direction == "right":
        new_pos = (player_pos[0], player_pos[1] + 1)
    else:
        return player_pos  
    
   
    if is_valid_move(new_pos):
        return new_pos
    else:
        print("Invalid move.")
        return player_pos

def main():
    
    start_pos, exit_pos = create_dungeon()
    player_pos = start_pos
    move_count = 0

    print("Welcome to the dungeon!")
    print("This is the grid  (P = player . = empty):")
    
    while player_pos != exit_pos:
        display_dungeon(player_pos, exit_pos)
        print(f"\nYou are at {player_pos}. Move count: {move_count}")
        
        
        move = input("Enter your move (up, down, left, right) or 'exit' to stop: ").strip().lower()

        if move == "exit":
            
            print("The end.")
            success = False
            break

       
        player_pos = move_player(player_pos, move)
        move_count += 1

    else:
        
        print(" you have reached the end")
        success = True
    
    
    with open("dungeon_result.txt", "w") as file:
        file.write(f"Success: {success}")
        file.write(f"Total moves: {move_count}")

    print(f"Game over! Success: {success}, Total moves: {move_count}")

if __name__ == "__main__":
    main()

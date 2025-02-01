# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:42:48 2025

@author: erhess
"""

import pandas as pd


file_path = r"C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/poke (2).csv"
df = pd.read_csv(file_path)


def is_number(input_value):
    try:
        int(input_value)  
        return True
    except ValueError:
        return False


user_input = input("Please enter a number: ").strip()


if not is_number(user_input):
    print("Please provide a number")
 
    user_input = input("Please enter a number: ").strip()
    
    
    if not is_number(user_input):
        print("Error")
        exit()  


index = int(user_input)  


if index < len(df) and index >= 0:
  
    pokemon_at_index = df.iloc[index]
    
    
    pokemon_with_id = df[df['id'] == pokemon_at_index['id']]

    
    combined_data = pd.concat([pokemon_at_index.to_frame().T, pokemon_with_id])


    print(combined_data)
else:
    print("Index out of range")


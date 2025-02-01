# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:18:32 2025

@author: erhess
"""

import pandas as pd


file_path = r"C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/poke (2).csv"
df = pd.read_csv(file_path)

name = input("Enter the name of the pokemon: ").strip()


data = df[df['identifier'].str.lower() == name.lower()]


print(f"Data for {name}:")


    
    
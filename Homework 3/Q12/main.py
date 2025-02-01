# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:47:52 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/poke (2).csv")
locations_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/locations-2.csv")
regions_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/regions.csv")

def search_by_name(poke_df):
    pokemon_name = input("Enter the name of the Pokemon: ").strip().lower()
    
    result = poke_df[poke_df['identifier'].str.lower() == pokemon_name]
    
    if result.empty:
        print(f"Sorry, the mysterious Pokemon '{pokemon_name}' cannot be found.")
    else:
        print("Pokemon Found:")
        print(result[['identifier', 'id', 'height', 'weight']])

def search_by_region(locations_df, regions_df):
    region_name = input("Enter the name of the region: ").strip().lower()
    
    region_result = regions_df[regions_df['region_name'].strip().lower() == region_name]
    
    if region_result.empty:
        print(f"Sorry, the region '{region_name}' does not exist.")
    else:
        region_id = region_result['region_id'].values[0]
       
        locations_in_region = locations_df[locations_df['region_id'] == region_id]
        
        if locations_in_region.empty:
            print(f"There are no locations in the region '{region_name}'.")
        else:
            print(f"Locations in {region_name}:")
            print(locations_in_region[['location']])

def main():
    print("Hello, Ash!")
    
    while True:
        print("1) Search By Name")
        print("2) Search By Region")
        print("3) Exit")
        choice = input("select an option: ").strip()
        
        if choice == '1':
            search_by_name(poke_df)
        elif choice == '2':
            search_by_region(locations_df, regions_df)
        elif choice == '3':
            print("Goodbye")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

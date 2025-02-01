# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:09:31 2025

@author: erhess
"""

import pandas as pd 

def main(): 
   
    region_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/regions.csv")
    location_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/locations-2.csv")
    
    
    region_name = input("Enter the name of the region: ").strip().lower()

    
    region = region_df[region_df['region_name'].str.lower() == region_name]
    
    if len(region) > 0:  
        region_id = region['region_id'].values[0]
        
        
        locations_in_region = location_df[location_df['region_id'] == region_id]
        
       
        print(f"The number of locations in {region_name} is: {len(locations_in_region)}")
    else:
        
        print("This region does not exist.")

if __name__ == "__main__":
    main()

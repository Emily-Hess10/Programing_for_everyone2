# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:30:56 2025

@author: erhess
"""

import pandas as pd

def main():
    
    region_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/regions.csv")
    locations_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/locations-2.csv")
    
   
    print("Columns in locations dataset:", locations_df.columns)
    
    
    locations_no_region = locations_df[(locations_df['region_id'] == '') | (locations_df['region_id'].isnull())]
    
    
    if len(locations_no_region) == 0:
        print("All locations have a region.")
    else:
        
        print("Locations with no region:")
        print(locations_no_region) 

if __name__ == "__main__":
    main()


    
    
   
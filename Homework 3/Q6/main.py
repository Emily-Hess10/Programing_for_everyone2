# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:45:56 2025

@author: erhess
"""

import pandas as pd


file_path = r"C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/Homework 3/Data/poke (2).csv"
df = pd.read_csv(file_path)


num_rows, num_columns = df.shape


column_names = df.columns.tolist()


print(f"It has {num_columns} columns and {num_rows} rows.")
print(f"It has the following column names: {column_names}")

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 15:42:23 2025

@author: erhess
"""

import pandas as pd


poke_df = pd.read_csv("C:/Users/erhess/OneDrive - Carlow University/Programing for evryone 2/EC1/data/poke1.csv")


poke_df["cleaned_name"] = poke_df["identifier"].str.split("-").str[-1].str.title()


poke_df["cleaned_name"].to_csv("q12.out", index=False, header=False)


print(poke_df["cleaned_name"])

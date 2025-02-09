# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:17:25 2025

@author: erhess
"""

import pandas as pd

poke_df = pd.read_csv("../data/poke1.csv")


poke_df["cleaned_name"] = poke_df["identifier"].str.replace("-", " ").str.title()


poke_df["cleaned_name"].to_csv("q12.out")


print(poke_df["cleaned_name"])

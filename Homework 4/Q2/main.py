# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:54:36 2025

@author: erhess
"""


import pandas as pd


locations_df = pd.read_csv("../data/locations.csv")
regions_df = pd.read_csv("../data/regions.csv")


locations_df["region_id"].fillna(999, inplace=True)


locations_df.to_csv("q2-a.out", index=False)


new_region = pd.DataFrame({"id": [999], "identifier": ["Carlow"]})


regions_df = pd.concat([regions_df, new_region], ignore_index=True)


regions_df.to_csv("q2-b.out", index=False)


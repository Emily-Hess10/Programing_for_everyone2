# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:43:44 2025

@author: erhess
"""

import pandas as pd


df = pd.read_csv("../data/locations.csv")


null_rows = df[df.isnull().any(axis=1)]


null_rows.to_csv("q1.out", index=False)

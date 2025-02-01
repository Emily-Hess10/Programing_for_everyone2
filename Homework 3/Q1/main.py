# main.py
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

user_test = [{"Name": "Alice", "score": "78"},
             {"Name": "Emily", "score": "100"},
              {"Name": "Grace", "score": "88"},
               {"Name": "Caleb", "score": "85"},
    ]

df = pd.DataFrame(user_test)

print(df["Name"])
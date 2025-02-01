# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:00:07 2025

@author: erhess
"""

#main.py


import pandas as pd

df = pd.DataFrame(columns=['user', 'score'])


def opening():
    print("a: Add score")
    print("b: Check scores")
    print("c: Exit")


while True:
    opening()  
    answer = input("What would you like to do: ").lower().strip()  

    if answer == "a":
        user = input("add user name: ").strip()
        score = input("add score: ").strip()

       
        df = df.append({"user": user, "score": score}, ignore_index=True)
        print(f"Score added for {user}.")

    elif answer == "b":
       check = input("Please enter the name of the user to check: ").strip()
       user_scores = df[df['user'] == check]

       print(f"Scores for {check}:")
       print(user_scores)
        
        
    elif answer == "c":
       
        print("Exit.")
        break

    else:
        print("pick a, b, or c")
      


        
        
    
    
    
    
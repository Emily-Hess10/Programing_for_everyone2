# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:38:36 2025

@author: erhess
"""

import pandas as pd


df = pd.DataFrame(columns=['user', 'score'])


def opening():
    print("a: Add score")
    print("b: Check scores")
    print("c: Show scores")
    print("d: Exit")


while True:
    opening()  
    answer = input("What would you like to do: ").lower().strip()  

    if answer == "a":
        user = input("Add user name: ").strip()
        score = input("Add score: ").strip()

        df = df.append({"user": user, "score": score}, ignore_index=True)
        print(f"Score added for {user}.")

    elif answer == "b":
        
        check = input("Please enter the name of the user to check: ").strip()
        user_scores = df[df['user'] == check]

        if not user_scores.empty:
            print("Scores for {check}:")
            print(user_scores)
        else:
            print("No scores found for {check}.")

    elif answer == "c":
        print("Total scores:")
        if not df.empty:
            print(df)
        else:
            print("No scores available yet.")

    elif answer == "d":
        
        print("Exit.")
        break

    else:
        print("pick a, b, c, or d.")


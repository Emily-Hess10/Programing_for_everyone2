# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:36:39 2025

@author: erhess
"""
#Q2 Age homework 1

age = input("Enter your age: ")


age = int(age)

with open("q2.out", "w") as file:
    
    file.write(f"Original age: {age}")
    

    new_age = age + 5
    
    print(new_age)
    file.write(f"Age + 5 years: {new_age}")

print("Data has been written to q2.out")
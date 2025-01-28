# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:37:07 2025

@author: erhess
"""
#Q3 age Homework 1

age = int(input("Enter your age: "))

with open("q3.out", "w") as file:
    if age < 20:
        file.write("fail to write to q3.out") 
        print("fail to write to q3.out") 
    elif 20 <= age <= 30:
        file.write("pass to q3.out")  
        print("pass to q3.out")
    else:
        file.write("fail to write to q3.out") 
        print("fail to write to q3.out") 
 
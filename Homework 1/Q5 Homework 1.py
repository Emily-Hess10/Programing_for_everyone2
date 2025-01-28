# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:39:52 2025

@author: erhess
"""

#Q4 Name Homework 1
names= []

while True:
   
    name = input("Enter a name or type exit to stop: ")
    
    
    if name.lower() == "exit":
        break
    
   
    names.append(name)


with open("q4.out", "w") as file:
    for name in names:
        file.write(name)

print("List of names has been written to q4.out")
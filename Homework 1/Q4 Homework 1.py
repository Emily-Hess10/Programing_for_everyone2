# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:37:36 2025

@author: erhess
"""

#Q5 List Homework 1 
def opening():
    print("Hello")
    print(""" 
          1. Enter user
          2. Exit
          """)

def main():
    user_name = []  
    
    while True:
        opening()  
        choice = input("What do you want to do: ")  
        
        if choice == "1":
            name = input("Enter name: ")  
            user_name.append(name)  
            print(f"User {name} added.")
        
        elif choice == "2":
            print("Exiting. Here are the names:")
            
            for name in user_name:
                print(name)
            
            
            with open("q5.out", "w") as file:
                for name in user_name:
                    file.write(name)
            
            print("List of users has been written to q5.out.")
            break  
        
        else:
            print("Invalid choice. Please choose 1 or 2.")


main()
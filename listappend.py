# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:50:04 2023

@author: Kairu Cyrus
"""

members_list = []
while True:
    name = input("Enter name: ")
    
    id_no = int(input("Enter ID number: ")) #no exceptions handled in the case a user enters a non-integer
    
    plot_no = int(input("Enter plot number: "))
    members_list.append((name,id_no,plot_no))
    more = None
    while True:
        more = input("Add another? (Y?N): ").upper()
        if more in ("Y", "N"):
            break
        print("Invalid input")
    if more == "N":
        break
print(members_list)






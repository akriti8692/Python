# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:34:46 2020

@author: 16509
"""

#Question5, no of organism

startd=float(input("Enter no of organism on the start day"))
pinc=float(input("Enter the amount increases"))
days=int(input("Number of days to multiply"))

for i in range(1,days+1):
    print("day",i,"Organism value",startd)
    startd=startd+(startd)*(pinc)/100


print("End of loop")



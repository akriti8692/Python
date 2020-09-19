# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:47:09 2020

@author: 16509
"""

input1=0
C=0
F=0
A=0

def display_menu():
    input1=input("Indicate which temperature conversion you would like to perform, by entering 1 or 2,1. Fahrenheit to Celsius2. Celsius to Fahrenheit")
    return input1

def convert_temp(A):
    if (A=='1'):
        F=int(input("Enter Fahrenheit value"))
        C= (5/9*(F - 32))
        print(C)
    elif (A=='2'):
        C=int(input("Enter Celcius Value"))
        F = C*9/5 + 32
        print(F)
    else:
        print("Invalid Input")
    
def main():
    A = display_menu()
    convert_temp(A)

main()    
        
        
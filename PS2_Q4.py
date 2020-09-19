# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:37:41 2020

@author: 16509
"""

#Question4
#PArt1
WUSA=(1991, 1999, 2015, 2019)
#Part2
print('First year USA won World Cup',WUSA[0])
print('First three years USA won World Cup are',WUSA[0:3])

#Part3
WWC_Winner={'United States','Norway','United States','Germany','Germany',
             'Japan','United States','United States'}
print(WWC_Winner)

#Part4-Yes,it can be added
WWC_Winner.add('United States')

#Part5-Yes,it can be added
WWC_Winner.add('Ghana')

print(WWC_Winner)




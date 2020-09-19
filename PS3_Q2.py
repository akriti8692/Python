# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:51:26 2020

@author: 16509
"""

veg=str(input("Is anyone in your party a vegetarian? Please answer by 'yes' or 'no'"))
vege=str(input("Is anyone in your party a vegan? Please answer by 'yes' or 'no'"))
gf=str(input("Is anyone in your party a gluten free? Please answer by 'yes' or 'no'"))

if (veg=='no' #and vege=='no'
    and gf=='no'):
    print('Burgers Madness')
      
if (veg=='yes' and vege=='yes' and gf=='yes'):
    print('Lovin Veggies')
      
if (veg=='yes' #and vege=='no'
      and gf=='yes'):
    print('Pizza Mania')

if (veg =='yes' and vege=='yes' and gf=='no'):
    print('Napolita')
if (veg=='yes' and vege=='yes' and gf=='no'):
    print('Coffebucks')
if(veg=='yes' 
     #and vege=='no'
     and gf=='no'):
    print('Mama Kitchen')
    
    #unable to get the first part as per the PS
    
    
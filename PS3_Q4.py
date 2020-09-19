# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:24:31 2020

@author: 16509
"""
#Question4
c=[]
temp=[73,70,79,79,72,72,70]

for i in temp:
    k=round(((5.0/9.0)*(i-32)),2)
    c.append(k)
    
lowest=c[0]
highest=c[0]
for i in range(0,7):
    if c[i]<lowest:
        lowest=c[i]
    if c[i]>highest:
        highest=c[i]
        
print("Lowest is ",lowest)
print("Highest is ",highest)
print(c)


#Question5

        
        
        
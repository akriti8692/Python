# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:03:29 2020

@author: 16509
"""

var=[]
for s1 in range(1,20):
    for s2 in range(s1,20):
        for s3 in range(s2,20):
            if (s1*s1 + s2*s2 == s3*s3):
                print (s1, s2, s3)
                    
print("End of loop")
 
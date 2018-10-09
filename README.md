# "schludny kod pod "raw""
# ps mam troche pytań

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 00:41:36 2018

@author: HP
"""

def sred(n):
    return(sum(n)/len(n))
 
print(sred([2,2,2,2,2,2]) - 2 < 0.0000001)
print(sred([4, 6, 55, 18, 17, 12]) - 18.666666666666668 < 0.0000001)
print(sred([86, 89, 24, 45, 62, 17, 61, 63, 30, 13]) - 49 < 0.0000001)

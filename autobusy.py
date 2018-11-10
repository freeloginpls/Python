# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:46:11 2018

@author: HP
"""
import numpy as np
a=[1, 2, 1, 1, 1, 2, 1, 3]
b=[1, 2, 1, 1, 1, 2, 1, 3,3]
c=[1,1,1,2,3,4,3,2,3,1,1,2,3,4,3,2]

#wiem, ze moge sprawdzac do połowy,a nie do sum(a)+1 -poki co tak

def autobus(a): 
        k=np.cumsum(a)
        odp=list()
        for i in range(1,sum(a)+1):
            if(i <max(a)):continue
            if(sum(a)%i !=0 ):continue
            if(set(q for q in range(sum(a)+1)   if q % i == 0 and q >0).issubset(k)) :
                odp.append(i)
        return(odp)        
            
print(autobus(a))
print(autobus(b))
print(autobus(c))
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:22:15 2018

@author: HP
"""

#zad1
from miszcz import funkcja

print(ciekawafunkcjawersjapython(665))    
print(ciekawafunkcjawersjapython(-2))
print(ciekawafunkcjawersjapython(0))

#zad2

def double(x):
    if isinstance(x, (int,float)):
        return((x,x*2))
    if isinstance(x,list):
        return((x*2,[i * 2 for i in x]))
    


x = 3.
print(double(x) == (3.0, 6.0))
print(x == 3.)
print(double(x))

z = [3]
print(double(z) == ([3, 3], [6]))
print(z == [3])
print(double(z))

w = [1, 2, 3]
print(double(w) == ([1, 2, 3, 1, 2, 3], [2, 4, 6]))
print(w == [1, 2, 3])


print(double(x))

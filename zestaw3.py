# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:03:29 2018

@author: HP
"""
#zad3
#metoda ksywa i ilosc_zadanek na potrzeby  4 zadanka
class Kolo:
    def __init__(self,pseudomin,zaplacil,n_zadan):
        self.pseudomin=pseudomin
        self.zaplacil=zaplacil
        self.n_zadan=n_zadan
    def zadanko_wincyj(self):
        self.n_zadan=int(self.n_zadan +1)
    def ksywa(self): 
        return self.pseudomin
    def ilosc_zadanek(self):
        return self.n_zadan
    

        
Jacek=Kolo('Rita Repulsa',zaplacil=True,n_zadan=1) # na potrzeby klasy :)
Kewin=Kolo('Lord Zed',zaplacil=True,n_zadan=3)
Damian=Kolo('Zordon',zaplacil=False,n_zadan=9001) 
print(Jacek.pseudomin,Jacek.zaplacil,Kewin.n_zadan)
print(Kewin.pseudomin,Kewin.zaplacil,Kewin.n_zadan)
print(Damian.pseudomin,Damian.zaplacil,Damian.n_zadan)

Damian.zadanko_wincyj() #kto mialby zrobic zadanie jak nie on :P
print(Damian.n_zadan)
print(Damian.ksywa())

#zad4
#podgrupa- czy czlonek podgrupy pythonowskiej
class DataRanger(Kolo):
    def __init__(self,pseudomin,zaplacil,n_zadan,podgrupa):
        Kolo.__init__(self,pseudomin,zaplacil,n_zadan)
        self.podgrupa=podgrupa
    def ksywa(self):
        print (Kolo.ksywa(self))
    def ilosc_zad(self):
        print (Kolo.ilosc_zadanek(self))
         

Gosia=DataRanger("Ranger69kg",True,5,"Tak")
print(Gosia.pseudomin,Gosia.zaplacil,Gosia.n_zadan,Gosia.podgrupa)   

print(Gosia.pseudomin )

Gosia.ksywa() 
Gosia.ilosc_zad()

#zad 5
import numpy as np
a=[1, 2, 1, 1, 1, 2, 1, 3]
b=[1, 2, 1, 1, 1, 2, 1, 3,3]
c=[1,1,1,2,3,4,3,2,3,1,1,2,3,4,3,2]

#wiem, ze moge sprawdzac do połowy,a nie do sum(a)+1 -poki co tak

def autobus(pasazer): 
        odp=list()
        for i in range(1,sum(pasazer)+1):
            if(sum(pasazer)%i !=0 ):continue
            if(set(q for q in range(sum(pasazer)+1)   if q % i == 0 and q >0).issubset(np.cumsum(pasazer))) :
                odp.append(i)
        return(odp)        
            
print(autobus(a))
print(autobus(b))
print(autobus(c))
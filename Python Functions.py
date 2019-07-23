# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:16:55 2019

@author: admin
"""
def gr2(x,y):
    if(x>y):
       print("{} is greater than y".format(x))
    else:
       print("{} is greater than x".format(y))

print(gr2(799,800))

#Multipy 5 by gretaest
def gr3(x,y,z):
  if(x>y & x>z): return x
  elif(y>z):return y
  else: return z
  
a=gr3(10,20,5)*5

#Rental
"""This function calculates Ebill (function documentation)"""
def Ebill(unit,rental=350):
    if(unit<=100):
        rent=unit*10+rental
        return rent
    elif(unit>100 & unit<=500):
        return(1000+(unit-100)*15+rental)
    else:
        return(1000+6000+(unit-500)*25+rental)
        
print(Ebill(20,100))
Ebill.__doc__
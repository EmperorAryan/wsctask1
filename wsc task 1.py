# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:11:33 2022

@author: agary
"""

n=int(input("Enter number of trades: "))
l=0
s=0
for i in range (n):
    q=input()
    if q.lower()=='long':
        l=l+1
    elif q.lower()=='short':
        s=s+1
    else: 
        print("enter only long or short")
        
print("Data: Long-> ", l, ", Short-> ", s)

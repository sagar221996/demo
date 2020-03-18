'''
Created on 09-Mar-2020

@author: sgatla

'''
from array import *

arr=array('i',[])
n=int(input("enter the number of values you want to enter"))
for i in range(n):
    a=int(input("Enter the values"))
    arr.append(a)
    
print(arr)


b=int(input("enter the value to be searched"))
k=0
for e in arr:
    if e==b:
        print("value found at \n position ", k)
    k+=1
        
        

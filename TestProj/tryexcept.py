'''
Created on 12-Mar-2020

@author: sgatla
'''
from _ast import Try
a=5
b=0

try:
    print(a/b)
    k=int(input("Enter a number"))
    
except ZeroDivisionError as e:
    print("You cannot divide number by zero:",e)
except ValueError as e:
    print("Invalid input")
    
except Exception as e:
    print(e)
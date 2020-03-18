'''
Created on 11-Mar-2020

@author: sgatla
'''



def rec(n):
    
    if n==0:
        return 1
    n=n*rec(n-1)
    
    
    return n

r=rec(4)
print(r)
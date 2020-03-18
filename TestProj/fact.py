'''
Created on 11-Mar-2020

@author: sgatla
'''
def facto(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        
    return f
r=facto(4)
print(r,"using ascending order")

def fact(j):
    f=1
    for i in range(j-1,1,-1):
        j=j*i
        
    return j
q=fact(4)
print(q,"using descending order")
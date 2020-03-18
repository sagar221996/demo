'''
Created on 11-Mar-2020

@author: sgatla
'''
from functools import *

nums=[2,3,4,5,6]

evens=list(filter(lambda n:n%2==0,nums))

print("output of filtering",evens)

doubles=list(map(lambda n:n*2,evens))
print("output of map",doubles)

sum=reduce(lambda a,b:a+b,doubles)

print("output of reduce",sum)

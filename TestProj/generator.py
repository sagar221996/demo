'''
Created on 12-Mar-2020

@author: sgatla
'''
from _sqlite3 import sqlite_version
def topten():
        j=1
        while j<=10:
            sq=j*j
            yield sq
            j+=1
  
    
    
values=topten()


print(values.__next__())
for i in values:
    print(i)
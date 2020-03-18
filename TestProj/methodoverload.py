'''
Created on 12-Mar-2020

@author: sgatla
'''
class Stud:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
            
        elif a!=None and b!=None:
            s=a+b
            
        else:
            s=a
            
        return s
        
s=Stud(68,72)
s2=Stud(42,54)


print(s.sum(2,4,6))
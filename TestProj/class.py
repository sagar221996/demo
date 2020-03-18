'''
Created on 11-Mar-2020

@author: sgatla
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self,c,r):
        self.c=c
        self.r=r
        
    def update(self):
        print("config is",self.c,self.r)
        

c1=MyClass('i5','2gb')

c1.update()

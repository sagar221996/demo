'''
Created on 12-Mar-2020

@author: sgatla
'''
from mimetypes import init
from test.test_isinstance import Super

class A():
   


    def __init__(self):
        print("A init")
        
        
    def feat1(self):
        print("feature 1")
        
        
class B():
    
    def __init__(self):
        #super().__init__()
        print("B init")
    
    def feat2(self):
        
        print("feature 2")
        
        
class C(A,B):
    
    def __init__(self):
        super().__init__()     #uses a concept of MRO i.e method resolution order
        print("c  init")
        
        
    def feat3(self):
        print("feature 3")
        
    
        
a=C()
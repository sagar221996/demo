'''
Created on 12-Mar-2020

@author: sgatla
'''
f=open('mydata','r')
print(f.read())

f2=open('copy','w')

for i in f:
    f2.write(i)
    print("successfull")
    
    
f3=open('copy','r')
print(f3.read())


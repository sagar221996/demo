'''
Created on 11-Mar-2020

@author: sgatla
'''


def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
    
    
lst=[]
a=int(input("Enter the no of values"))

for i in range(a):
    b=int(input("enter values"))
    lst.append(b)
    

print(lst)


even,odd=count(lst)

print("number of even no.:{} and number of odd no.:{}".format(even, odd))

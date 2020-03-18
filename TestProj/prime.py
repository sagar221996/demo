'''
Created on 29-Feb-2020

@author: sgatla
'''
x=int(input("Enter the number"))
for i in range(2,x):
    if x % i==0:
        print("The number is not prime")
        break
else:
    print("prime number")
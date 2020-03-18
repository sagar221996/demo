'''
Created on 11-Mar-2020

@author: sgatla
'''
def fibo(n):
    a=0
    b=1
    
    print(a)
    print(b)
    
    for i in range(0,n-2):
        c=a+b
        a=b
        b=c
        print(c)

n=int(input("Enter the number of values"))
fibo(n)



    
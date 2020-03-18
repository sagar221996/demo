x= input("Enter first number");
a=int(x);
y=input("Enter second number");
b=int(y);
c=a+b;
print(c);
x=c%2;
i=1;
while i<5:    
    if x==0:
        print("even number");
    else:
         print("odd number")   
    i=i+1
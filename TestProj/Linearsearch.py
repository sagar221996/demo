pos=-1
def search(lst,n):
    k=0
    for i in lst:
        if i==n:
            globals()['pos']=k
            return True
        k=k+1     
    
        
    return False







lst=[2,5,7,8,0]
n=5


if search(lst,n):
    print("found at position",pos+1)
else:
    print("not found")
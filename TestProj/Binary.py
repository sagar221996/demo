'''
Created on 12-Mar-2020

@author: sgatla
'''
pos=-1
def search(lst,n):
    l=0
    u=len(lst)
    
    while l<=u:
        mid=(l+u)//2
        if lst[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if lst[mid]<=n:
                l=mid+1
            else:
                u=mid-1

    return False
lst=[2,5,7,8,0]
n=5


if search(lst,n):
    print("found at position",pos+1)
else:
    print("not found")
def Sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp


lst=[2,6,7,3,41,2,4]
Sort(lst)
print(lst)




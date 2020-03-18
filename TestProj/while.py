"""
Created on 29-Feb-2020

@author: sgatla
"""
i=0;
l1=["jan ","feb ","mar ","apr ","may ","jun ","jul ","aug ","sep ","oct ","nov ","dec "];
l2=["sun ","mon ","tue ","wed ","thur ","fri ","sat ","sun "]
while i<=11:
    print(l1[i] ,end="")
    j=0
    while j<=6:
        print(l2[j] ,end="")
        j=j+1
    i=i+1
    print()
from math import *
t=int(input())
for b in range(t):
    m=input()
    h=int(sqrt(len(m)))
    l=[]
    for i in range(1,h+1):
        for j in range(1,h+1):
            l.append(m[j*h-i])
    print(*l,sep='')

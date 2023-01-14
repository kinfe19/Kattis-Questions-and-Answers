from math import factorial as f
n,m=[int(i)for i in input().split()]
l=[int(i)for i in input().split()]
d={}
for i in l:
    k=i//m
    try:
        d[k]+=1
    except:
        d[k]=1
c=0
for i in d:
    m=d[i]
    if m>=2:
        c+=f(m)//(f(2)*f(m-2))
print(c)
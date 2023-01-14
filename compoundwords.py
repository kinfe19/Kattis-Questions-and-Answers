from itertools import permutations as c
l=[]
while 1:
    try:
        l.extend(input().split())
    except:
        break
k=list(c(l,2))
p=[]
for i,j in k:
    p.append(i+j)
for i in sorted(set(p)):
    print(i)
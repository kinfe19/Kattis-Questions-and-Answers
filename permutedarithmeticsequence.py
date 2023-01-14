n = int(input())
for i in range(n):
    l = [int(j) for j in input().split()]
    l=l[1:];d=sorted(l)
    q=0;t=d[1]-d[0]
    for j in range(1,len(d)):
        if d[j]-d[j-1] != t: q=1
    if q:print('non-arithmetic')
    elif l==d or l[::-1]==d:print('arithmetic')
    else:print('permuted arithmetic')
n=int(input())
for i in range(n):
    a,b=[int(i)for i in input().split()]
    p=sum(range(0,b+1))
    print(a,p,2*p-b,2*p)


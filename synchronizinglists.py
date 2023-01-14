n=int(input())
while n!=0:
    l=[int(input())for i in range(n)]
    p=sorted(l)
    k=sorted([int(input())for i in range(n)])
    for i in l:
        print(k[p.index(i)])
    print()
    n=int(input())

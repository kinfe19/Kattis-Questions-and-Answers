n=int(input())
while n!=0:
    f=[]
    s=[]
    for i in range(n):
        j=input()
        s.append([j[:2],i])
        f.append(j)
    for i in sorted(s):
        print(f[s.index(i)])
    print()
    n=int(input())

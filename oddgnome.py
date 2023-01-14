n=int(input())
for i in range(n):
    l=[int(i)for i in input().split()]
    l=l[1:-1]
    for j in range(1,len(l)):
        if l[j]-l[j-1]!=1:
            print(j+1)
            break

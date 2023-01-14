n,r=[int(i)for i in input().split()]
l=[int(input())for i in range(r)]
k=range(1,n+1)
if n==r:
    print('too late')
else:
    for i in k:
        if i not in l:
            print(i)
            break

l=[int(i) for i in input().split()]
l.sort()
a=l[1]-l[0]
b=l[2]-l[1]
if a==b:
    print(l[2]+a)
elif a<b:
    print(l[1]+a)
else:
    print(l[0]+b)


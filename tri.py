def s(n):
    return str(n)
a,b,c=[int(i)for i in input().split()]
if a+b==c:
    print(s(a)+'+'+s(b)+'='+s(c))
elif a==b+c:
    print(s(a)+'='+s(b)+'+'+s(c))

elif a-b==c:
    print(s(a)+'-'+s(b)+'='+s(c))
elif a==b-c:
    print(s(a)+'='+s(b)+'-'+s(c))

elif a*b==c:
    print(s(a)+'*'+s(b)+'='+s(c))
elif a==b*c:
    print(s(a)+'='+s(b)+'*'+s(c))

elif b!=0 and a/b==c:
    print(s(a)+'/'+s(b)+'='+s(c))
elif c!=0 and a==b/c:
    print(s(a)+'='+s(b)+'/'+s(c))
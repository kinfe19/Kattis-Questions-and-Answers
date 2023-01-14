from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
while True:
    try:
        h=[int(i)for i in input().split()]
        while(len(h)!=1):
            a=h.pop()
            b=h.pop()
            h.append(lcm(a,b))
        print(h[0])
    except:
        break
cn = 10001
def nor(v, a, b):
    return (v*a + b) % cn

def fin(l):
    x, y, z = l[:3]
    for i in range(cn):
        if abs(z-y) == abs((i**2*(y-x)) % cn):
            for j in range(cn):
                f = 1
                for k in range(len(l)-1):
                    if nor(nor(l[k], i, j), i, j) != l[k+1]:
                        f = 0
                        break
                if f:
                    return i, j
    return 0, 0         

l= [int(input()) for _ in range(int(input()))]
if len(l)>2:
    a, b = fin(l)
    for i in l:
        print(nor(i, a, b))
else:
    for i in l:
        print(0)
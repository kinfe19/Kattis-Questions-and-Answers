from math import acos, pi

def ln(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5

def teta(a, b, c):
    return (acos((a*a+b*b-c*c)/ (a*b*2))) * 180 / pi

s = [int(i) for i in input().split()]
while s != [0]:
    n, *bac_p = s
    while len(bac_p) > 6:
        p = bac_p.copy()
        p.extend(p[:4])
        l = []
        for i in range(len(bac_p)//2):
            x1, y1, x2, y2, x3, y3 = p[i*2 : (i*2)+6]
            a = ln(x1, y1, x2, y2)
            b = ln(x2, y2, x3, y3)
            c = ln(x3, y3, x1, y1)
            l.append(teta(a, b, c))
        v = l[-1]
        l = [v] + l[:-1]
        n_mn = min(l)


        dx = l.index(n_mn)
        baa = bac_p[:2*dx] + bac_p[(2*dx)+2:]

        p = baa.copy()
        p.extend(p[:4])
        ll = []
        for i in range(len(baa)//2):
            x1, y1, x2, y2, x3, y3 = p[i*2 : (i*2)+6]
            a = ln(x1, y1, x2, y2)
            b = ln(x2, y2, x3, y3)
            c = ln(x3, y3, x1, y1)
            ll.append(teta(a, b, c))
        if min(ll) < min(l):
            break
        else:
            bac_p = baa



    print(len(bac_p)//2, *bac_p)
    s = [int(i) for i in input().split()]

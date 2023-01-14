n, t = map(int, input().split())
l = [int(i) for i in input().split()]

if t == 1:
    f = 1
    d = {}
    for i in range(len(l)):
        x = 7777 - l[i]
        try:
            b = d[x]
            f = 0
            break
        except:
            d[l[i]] = 1
    if f:
        print('No')
    else:
        print('Yes')
elif t == 2:
     d = {}
     p =  sorted(l)
     f = 1
     for i in p:
         try:
             b = d[i]
             f = 0
             break
         except:
            d[i] = 1

     if f:
         print('Unique')
     else:
         print('Contains duplicate')
elif t == 3:
    d = {}
    for i in l:
        try:
            d[i] += 1
        except:
            d[i] = 1
    p = []
    for i in d:
        if d[i] > n/2:
            p.append(i)
    if p == []:
        print(-1)
    else:
        print(*sorted(p))
elif t == 4:
    p = sorted(l)
    if n%2 == 0:
        print(p[n//2-1], p[n//2])
    else:
        print(p[n//2])
elif t == 5:
    p = sorted(l)
    for i in p:
        if i > 999:
            break
        elif i >=100:
            print(i, end=' ')


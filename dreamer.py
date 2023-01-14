def form(n):
    if len(str(n)) == 1:
        return '0'+str(n)
    else:
        return n

from itertools import permutations as per
import datetime as dt
bd = dt.datetime(2000, 1, 1)
td = dt.datetime(2020, 11, 26)
for i in range(int(input())):
    k = list(input().replace(' ', ''))
    p = 0
    nm = []
    for j in set(per(k, len(k))):
        yr = int(''.join(j[4:]))
        dy = int(j[0]+j[1])
        mn = int(j[2]+j[3])
        f = 0
        try:
            f = dt.datetime(yr, mn, dy)
        except:
            pass
        if f!=0 and f>=bd:
            p += 1
            if nm == []:
                nm = f
            elif f <= nm:
                nm = f
    if nm == []:
        print(0)
    else:
        print(p, form(nm.day), form(nm.month), form(nm.year))
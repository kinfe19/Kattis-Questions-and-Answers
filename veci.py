from itertools import permutations as per
l = list(input())
p = sorted(set([int(''.join(i)) for i in per(l, len(l))]))
h = p.index(int(''.join(l)))

if h+1 == len(p):
    print(0)
else:
    print(p[h+1])
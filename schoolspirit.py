t = 4/5
def c(p):
    s = 0
    for i in range(len(p)):
        s += p[i] * pow(t, i)
    return s / 5
from itertools import permutations as per
l = [int(input()) for i in range(int(input()))]
s = c(l)
k = []
for i in range(len(l)):
    f = l.copy()
    f.pop(i)
    k.append(c(f))
print(s, sum(k)/len(k))
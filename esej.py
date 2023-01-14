from itertools import  permutations as per
s = 'abcdefghijklmnopqrstuvwxyz'
l = []
p = 1

while len(l)<50000:
    for j in per(s, p):
        l.append(''.join(j))
    p += 1
l = list(set(l))
a, b = map(int, input().split())
print(*l[:b])
s, e, b = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
tr = [int(i) for i in input().split()]

for i in range(b):
    s += l[i]
    if s > tr[i]:
        v = s%tr[i]
        if v != 0:
            s += tr[i] - v
    else:
        s += tr[i] - s 
    s += t[i]
s += l[-1]
if s<= e:
    print('yes')
else:
    print('no')
    
def sim(a, b):
    p = [0, 0, 0, 0]
    for i in range(4):
        if a[i]==b[i]:
            p[i]=1
    return p
l = []
for i in range(4):
    l.extend(input().split())
v = []
for i in range(12):
    for j in range(i+1, 12):
        for k in range(j+1, 12):
            a = sim(l[i], l[j])
            b = sim(l[j], l[k])
            c = sim(l[i], l[k])
            if  a==b and b==c and a==c :
                v.append([i+1, j+1, k+1])
if v==[]:
    print('no sets')
else:
    for i in v:
        print(*i)
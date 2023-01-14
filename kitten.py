n = int(input())
d = {}
k = [int(i) for i in input().split()]
d[k[0]] = k[1:]
while k != [-1]:
    d[k[0]] = k[1:]
    k = [int(i) for i in input().split()]
v = [n]
fl = 1
while fl:
    for x, i in enumerate(d):
        if n in d[i]:
            v.append(i)
            n = i
            break
        if x==len(d)-1:
            fl=0
print(*v)
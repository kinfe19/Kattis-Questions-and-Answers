n = input()
b = set(n)
d = []
if len(b) < 3:
    print(0)
else:
    for i in b:
        d.append(n.count(i))
    d.sort()
    print(sum(d[:-2]))
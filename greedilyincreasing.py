input()
l = [int(i) for i in input().split()]
d = [l[0]]
for i in l[1:]:
    if i > d[-1]:
        d.append(i)
print(len(d))
print(*d)
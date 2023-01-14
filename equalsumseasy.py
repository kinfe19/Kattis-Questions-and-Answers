from itertools import combinations as cm
t = int(input())
for _ in range(t):
    l = [int(i) for i in input().split()][1:]
    c = []
    for i in range(1, 20):
        c.extend(list(cm(l, i)))
    p = []
    for x, i in enumerate(c):
        d = sum(i)
        if d in p:
            r = p.index(d)
            print(f'Case #{_+1}:')
            print(*c[r])
            print(*i)
            break
        p.append(d)
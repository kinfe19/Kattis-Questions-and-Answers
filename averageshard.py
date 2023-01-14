t = int(input())
input()
for _ in range(t):
    c, e = [int(i) for i in input().split()]
    lc = [int(i) for i in input().split()]
    le = [int(i) for i in input().split()]

    ac = sum(lc)/c
    ae = sum(le)/e
    cn = 0
    for i in lc:
        if i<ac and i>ae:
            cn += 1
    print(cn)
    if _ != t-1:
        input()
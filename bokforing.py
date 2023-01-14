n, m = [int(i) for i in input().split()]
rr = 0
d = {}
for i in range(m):
    s, *r = input().split()
    if s == 'SET':
        d[int(r[0])-1] = int(r[1])
    elif s=="RESTART":
        rr = int(r[0])
        d = {}
    else:
        v = int(r[0])
        try:
            print(d[v-1])
        except:
            print(rr)
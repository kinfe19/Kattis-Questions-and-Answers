l = ['qwertyuiop', 'asdfghjkl ', 'zxcvbnm  ']
def dx(z):
    for j, i in enumerate(l):
        if z in i:
            return j, list(i).index(z)
def chds(a, b):
    s = 0
    for i in range(len(a)):
        x, y = dx(a[i]), dx(b[i])
        s += abs(x[0]-y[0])+abs(x[1]-y[1])
    return s
for i in range(int(input())):
    m, n = input().split()
    d = {}
    for j in range(int(n)):
        k = input()
        d[k] = chds(m, k)
    #dd = dict(sorted(d.items(), key=lambda item: item[1]))
    dd = dict(sorted(d.items(), key=lambda x: (x[1],x[0])))
    for i, j in dd.items():
        print(i, j)
    
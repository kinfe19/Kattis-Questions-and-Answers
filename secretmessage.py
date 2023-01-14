from math import ceil
n = int(input())
for i in range(n):
    k = input(); l = len(k)
    m = ceil(l ** 0.5)
    k += '*' * (m**2 - l)
    h = [];f=''
    for j in range(len(k)):
        if (j+1) % m == 0:
            h.append(f+k[j]);f=''
        else:f+=k[j]
    h = h[::-1]
    g = ''
    for i in range(m):
        for j in range(m):
            if h[j][i] != '*':
                g+=h[j][i]
    print(g)
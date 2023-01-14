n, m = map(int, input().split())
v = []
l = []
for i in range(n):
    s = input()
    for x, j in enumerate(s):
        if j == 'V':
            v.append([i, x])
    l.append(list(s))

def gor(p):
    if p[0]+1==n:
        return
    else:
        x, y = p
        v = l[x+1][y]
        if v == '.':
            l[x+1][y] = 'V'
            gor([x+1, y])
        elif v == '#':
            if y+1<m and l[x][y+1]=='.':
                l[x][y+1] = 'V'
                gor([x, y+1])
            if y>0 and l[x][y-1]=='.':
                l[x][y-1] = 'V'
                gor([x, y-1])           
        
for i in v:
    gor(i) 
for i in l:
    print(*i, sep='')
rh = input()
fn = []
for j in range(int(input())):
    g = input().split()
    for i in range(len(rh)):
        if rh[-(i+1):] in g:
            fn.extend(g)
            break
        
for j in range(int(input())):
    g = input().split()[-1]
    fl = 0
    for j in range(len(g)):
        if g[-(j+1):] in fn:
            fl = 1
            break
    if fl:
        print('YES')
    else:
        print('NO')
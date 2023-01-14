rw, cl = [int(i) for i in input().split()]
vals = [0, 0, 0, 0, 0]
l = []
for i in range(rw):
    l.append(list(input()))
for i in range(rw-1):
    for j in range(cl-1):
        nm = 0
        a = l[i][j];b=l[i+1][j];c=l[i][j+1];d=l[i+1][j+1]
        if a=='#' or b=='#' or c=='#' or d=='#':
            continue
        if a=='X':nm+=1
        if b=='X':nm+=1
        if c=='X':nm+=1
        if d=='X':nm+=1
        vals[nm]+=1
for i in vals:
    print(i)
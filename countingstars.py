case = 1
while True:
    try:
        n, m = [int(i) for i in input().split()]
        l = [list(input()) for i in range(n)]
        cn = 0
        sta = []
        for i in range(n):
            for j in range(m):
                if l[i][j]=='-':
                    cn += 1
                    sta.append((i, j))
                    while sta!=[]:
                        a = sta[-1][0]
                        b = sta[-1][1]
                        sta = sta[:-1]
                        l[a][b] = 'x'
                        if a-1 >= 0 and l[a-1][b]=='-':
                            sta.append((a-1, b))
                            
                        if a+1<n and l[a+1][b]=='-':
                            sta.append((a+1, b))
                            
                        if b-1>=0 and l[a][b-1]=='-':
                            sta.append((a, b-1))
                            
                        if b+1<m and l[a][b+1]=='-':
                            sta.append((a, b+1))
        print(f'Case {case}: {cn}')
        case += 1
    except:
        break

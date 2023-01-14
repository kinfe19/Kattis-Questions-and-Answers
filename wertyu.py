l = list("`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./")
while 1:
    try:
        s = input().split()
        p = []
        for i in s:
            x = ''
            for j in i:
                x+=l[l.index(j)-1]
            p.append(x)
        print(' '.join(p))
    except:
        break
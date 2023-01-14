sh = 0
co = 0
vl = 0
while 1:
    try:
        q = input().split()
        if q[0] == 'buy':
            s = int(q[1])
            c = int(q[2])
            co = (c*s + co*sh) / (sh+s)
            sh += s
            
        elif q[0] == 'sell':
            s = int(q[1])
            v = int(q[2])
            sh -= s
            vl -= v
            
        elif q[0] == 'split':
            v = int(q[1])
            sh *= v
            co /= v
            
        elif q[0] == 'merge':
            v = int(q[1])
            sh //= v
            co *= v
            
        else:
            v = int(q[1])
            t = 0
            if v>co:
                t = v - co
            print(sh * (v - (t*.3)))
            break
    except:
        break
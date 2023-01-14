for _ in range(int(input())):
    s = input().split()
    t, w, d, l, p = s
    if s.count('?') == 1:
        if t == '?':
            t = str(int(w)+int(d)+int(l))
        elif w == '?':
            w = str(int(t)-int(d)-int(l))
        elif d == '?':
            d = str(int(t)-int(w)-int(l))
        elif l == '?':
            l = str(int(t)-int(w)-int(d))
        elif p == '?':
            p = str(int(w)*3 + int(d))
    elif s.count('?') == 2:
        if t == '?' and w =='?':
            w = str((int(p)-int(d)) // 3)
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and d == '?':
            d = str(int(p) - int(w)*3)
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and l == '?':
            l = '0'
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and p == '?':
            p = str(int(w)*3 + int(d))
            t = str(int(w)+int(d)+int(l))
        elif w == '?' and d == '?':
            w = str((int(p)+int(l)-int(t))//2)
            d = str(int(p) - int(w)*3)
        elif w == '?' and l == '?':
            w = str((int(p)-int(d)) // 3)
            l = str(int(t)-int(w)-int(d))
        elif w == '?' and p == '?':
            w = str(int(t)-int(d)-int(l))
            p = str(int(w)*3 + int(d))
        elif d == '?' and l == '?':
            d = str(int(p) - int(w)*3)
            l = str(int(t)-int(w)-int(d))
        elif d == '?' and p == '?':
            d = str(int(t)-int(w)-int(l))
            p = str(int(w)*3 + int(d))
        elif l and p == '?':
            p = str(int(w)*3 + int(d))
            l = str(int(t)-int(w)-int(d))
    elif s.count('?') == 3:
        if t == '?' and w == '?' and d == '?':
            w = str(int(p) // 3)
            d = str(int(p) % 3)
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and w == '?' and l == '?':
            w = str((int(p)-int(d)) //3)
            l = '0'
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and w == '?' and p == '?':
            p = d
            w = '0'
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and d == '?' and l == '?':
            d = str(int(p) - int(w)*3)
            l = '0'
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and d == '?' and p == '?':
            p = str(int(w)*3)
            d = '0'
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and l == '?' and p == '?':
            p = str(int(w)*3 + int(d))
            l = '0'
            t = str(int(w)+int(d)+int(l))
        elif w == '?' and d == '?' and l == '?':
            w = str(int(p) // 3)
            d = str(int(p) % 3)
            l = str(int(t)-int(w)-int(d))
        elif w == '?' and d == '?' and p == '?':
            w = '0'
            d = '0'
            p = '0'
        elif w == '?' and l == '?' and p == '?':
            w = '0'
            l = '0'
            p = d
        elif d == '?' and l == '?' and p == '?':
            d = '0'
            l = '0'
            p = str(int(w)*3)
    elif s.count('?') == 4:
        if t == '?' and w == '?' and d == '?' and l == '?':
            w = str(int(p) // 3)
            d = str(int(p) % 3)
            l = '0'
            t = str(int(w)+int(d)+int(l))
        elif t == '?' and w == '?' and d == '?' and p == '?':
            w = '0'
            d = '0'
            p = '0'
            t = l
        elif t == '?' and w == '?' and l == '?' and p == '?':
            w = '0'
            l = '0'
            p = d
            t = d
        elif t == '?' and d == '?' and l == '?' and p == '?':
            d = '0'
            l = '0'
            p = str(int(w)*3)
            t = w
        elif w == '?' and d == '?' and l == '?' and p == '?':
            w = '0'
            d = '0'
            l = '0'
            p = '0'
    elif s.count('?') == 5:
        t = '0'
        w = '0'
        d = '0'
        l = '0'
        p = '0'
            
            
    print(t, w, d, l, p)


def dev(a, b):
    s = ''
    t = 1
    while 1:
        if not t and len(s[s.index('.'):]) == 8:
            break
        if a<b:
            if t:
                t = 0
                if s == '':
                    s += '0.'
                else:
                    s += '.'
            c, a = divmod(a*10, b)
            s += str(c)
        else:
            c, a = divmod(a, b)
            s += str(c)
    return s
a, b, c = [int(i) for i in input().split()]
print(dev(a*b, c))
while 1:
    try:
        l = input().split()
        n = []
        s = []
        for i in l:
            if i.isalpha():
                s.append(i)
            else:
                n.append(float(i))
        print(sum(n)/len(n), *s)
    except:
        break
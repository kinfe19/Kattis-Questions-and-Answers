while 1:
    try:
        l=[int(i)for i in input().split()]
        for i in range(len(l)):
            k=l.copy()
            k.remove(l[i])
            if sum(k)==l[i]:
                print(l[i])
                break 
    except:
        break
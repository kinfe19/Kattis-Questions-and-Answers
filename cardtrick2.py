f = list('abcdefghijklmnopqrstuvwxyz')
for z in range(int(input())):
    d = {}
    
    n = int(input())
    l = f[:n]

    i = 1
    while l != []:
        for v in range(i):
            v = l[0]
            l = l[1:]
            l.append(v)
        
        d[l[0]] = i
        l = l[1:]
        i+=1

    if l!=[]:
        for j in l:
            d[j]=i
            i+=1
    for i in f[:n]:
        print(d[i], end=' ')
    print()
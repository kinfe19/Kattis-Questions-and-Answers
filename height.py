for _ in range(int(input())):
    l = [int(i) for i in input().split()][1:]
    p = sorted(l)
    cn = 0
    while l != p:
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                if l[i]>l[j]:
                    l[i], l[j] = l[j], l[i]
                    cn += 1
    print(_+1, cn)
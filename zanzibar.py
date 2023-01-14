for _ in range(int(input())):
    l = [int(i) for i in input().split()]
    d = l[0]
    c = 0
    for i in range(1, len(l)):
        if l[i] > 2*d:
            c +=l[i] - 2*d
        d = l[i]
    print(c)
l = [float(i) for i in input().split()]
while len(l)!=1:
    x1, y1, x2, y2, p = l
    k = pow((abs(x2-x1)**p + abs(y2-y1)**p), (1/p))
    print('%.10f'%k)
    l = [float(i) for i in input().split()]
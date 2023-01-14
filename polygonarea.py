n = int(input())
while n!=0:
    l = []
    for _ in range(n):
        x, y = [int(i) for i in input().split()]
        l.append((x, y))
    sm = 0
    for i in range(n-1):
        x1, y1 = l[i]
        x2, y2 = l[i+1]
        sm += x1*y2 - x2*y1
    sm += l[-1][0]*l[0][1] - l[-1][1]*l[0][0]
    v = abs(sm/2)
    if sm<0:
        print('CW', v)
    else:
        print('CCW', v)
    n = int(input())
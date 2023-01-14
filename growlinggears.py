for _ in range(int(input())):
    mx = 0
    nx = 1
    for i in range(int(input())):
        a, b, c = [int(i) for i in input().split()]
        d = b*b / (4*a) + c
        if d > mx:
            mx = d
            nx = i+1
    print(nx)
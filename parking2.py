for _ in range(int(input())):
    n = int(input())
    l = sorted([int(i) for i in input().split()])
    s = 0
    for i in range(1, n):
        s += l[i] - l[i-1]
    print(2*s)
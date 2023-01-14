for _ in range(int(input())):
    n, *l = [int(i) for i in input().split()]
    print(sum(l) - n+1)
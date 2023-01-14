n = int(input())
while n != -1:
    l = [[int(i) for i in input().split()] for _ in range(n)]
    for i in range(n):
        fl = 0
        for j in range(n):
            if l[i][j]:
                for k in range(j+1, n):
                    if l[j][k] and l[i][k]:
                        fl = 1
                        break
            if fl:
                break
        if not fl:
            print(i, end=' ')
    print()
    n = int(input())
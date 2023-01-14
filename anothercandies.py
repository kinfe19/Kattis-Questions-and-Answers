for _ in range(int(input())):
    input()
    l = [int(input()) for __ in range(int(input()))]
    if sum(l) % len(l) == 0:
        print('YES')
    else:
        print('NO')
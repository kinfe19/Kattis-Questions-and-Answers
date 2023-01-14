r, c, n, m = [int(i) for i in input().split()]

l = [input() for i in range(r)]

for i in l:
    for j in range(n):
        for k in i:
            print(k*m, end='')
        print()
n = int(input())
l = [int(i) for i in input().split()]
p = sorted([(i, x+1) for x, i in enumerate(l)], reverse=True)
if p[0][0] <= sum([i for i, _ in p][1:]):
    for _, i in p:
        print(i, end=' ')
    print()
else:
    print('impossible')
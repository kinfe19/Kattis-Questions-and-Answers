a,b = [int(i) for i in input().split()]
c,d = [int(i) for i in input().split()]
t = int(input())
x = abs(a-c) + abs(b-d)
if t < x:
    print('N')
else:
    x = t - x - 1
    if x%2 == 1:
        print('Y')
    else:
        print('N')
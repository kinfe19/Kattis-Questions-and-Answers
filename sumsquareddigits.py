def tob(n, b):
    o = ''
    while n >0:
        o += str(n%b)+' '
        n = n//b
    return o

for _ in range(int(input())):
    t, b, n = [int(i) for i in input().split()]
    s = 0
    for i in tob(n, b).split():
        s+=int(i)**2
    print(t, s)
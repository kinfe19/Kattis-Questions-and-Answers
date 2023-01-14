a, b, c = [int(i) for i in input().split()]

d = 0
h = 0
while 1:
    d += 1
    h += a
    if h >= c:
        break
    h -= b
print(d)
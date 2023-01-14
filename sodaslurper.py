a, b, c = [int(i) for i in input().split()]
s = a+b

d = 0
r = 0
while 1:
    r = s % c if s!=0 else 0
    s //= c
    if s == 0:
        break
    d += s
    s += r
    
print(d)
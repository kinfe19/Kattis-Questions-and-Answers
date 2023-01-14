n = int(input())
f = True
for _ in range(n):
    k = int(_)**2 + n
    if k**.5 == int(k**.5):
        f = False
        break
if f:
    print('impossible')
else:
    print(_, int((int(_)**2 + n)**.5))
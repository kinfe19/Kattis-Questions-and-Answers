n = int(input())
p = input()
m = int(input())

s = 'abcdefghijklmnopqrstuvwxyz'
ln = len(p)
k = 0

for _ in range(m):
    x = 0
    t = ''
    for i in p:
        o = s[(s.index(i)+n)%26]
        if o in ['a', 'e', 'i', 'o', 'u', 'y']:
            x += 1
        t += o
    p = t
    if 2*x >= ln-x:
        k += 1
if k >= m-k:
    print('Colleague')
else:
    print('Boris')
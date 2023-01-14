d = []
for i in range(8):
    for j, x in enumerate(input()):
        if x == '*':
            d.append([i, j])
f = 1
for _ in range(len(d)):
    for __ in range(_+1, len(d)):
        a, b = d[_]
        i, j = d[__]
        if abs(a-i) == abs(b-j):
            f = 0
            break
if f and len(set([i[0] for i in d]))==8  and len(set([i[1] for i in d]))==8:
    print('valid')
else:
    print('invalid')

        


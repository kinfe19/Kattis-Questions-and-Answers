a = input()
b = input()
ln = max(len(a), len(b))
a = '0'*(ln-len(a)) + a
b = '0'*(ln-len(b)) + b
ca = ''
cb = ''
for i in range(ln):
    if a[i] > b[i]:
        ca += a[i]
    elif a[i] < b[i]:
        cb += b[i]
    else:
        ca += a[i]
        cb += b[i]
if ca=='':
    print('YODA')
else:
    print(int(ca))
if cb=='':
    print('YODA')
else:
    print(int(cb))
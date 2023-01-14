s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def r(a):
    k = [s.index(i) for i in a]
    sm = sum(k)
    return [(sm+i)%26 for i in k]
    
t = input()
ln = len(t)//2
a, b = r(t[:ln]), r(t[ln:])
for i in range(ln):
    print(s[(a[i]+b[i])%26], end='')
print()

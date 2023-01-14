def ex1(l, n, vl):
    l = list(l)
    l[n] = vl
    l = ''.join(l)
    return l

def ex2(l, a, b, vl):
    l = list(l)
    d = '?'
    if vl == 'or':
        if l[a] == '1' or l[b] == '1':
            d = '1'
        elif l[a] != '?' and l[b] != '?':
            d = str(int(l[a]) or int(l[b]))
    if vl == 'and':
        if l[a] == '0' or l[b] == '0':
            d = '0'
        elif l[a] != '?' and l[b] != '?':
            d = str(int(l[a]) and int(l[b]))
    l[a] = d
    return ''.join(l)

def tra(st, l):
    st = st.split()
    if st[0] == 'SET':
        l = ex1(l, int(st[1]), '1')
    elif st[0] == 'CLEAR':
        l = ex1(l, int(st[1]), '0')
    elif st[0] == 'OR':
        l = ex2(l, int(st[1]), int(st[2]), 'or')
    elif st[0] == 'AND':
        l = ex2(l, int(st[1]), int(st[2]), 'and')
    return l

n = int(input())
while n!=0:
    l = '?' * 32
    for i in range(n):
        l = tra(input(), l)
    print(l[::-1])
    n = int(input())
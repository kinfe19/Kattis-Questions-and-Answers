def m_t(n):
    a, b = [int(i) for i in n.split(':')]
    return a * 60 + b
def t_m(n):
    m = n // 60
    s = (n - m*60)
    if s < 0:
        s = 0
    s = str(s)
    if len(s) == 1:
        s = '0'+s
    return str(m)+':'+s
h = 0
a = 0
lh = 0
la = 0
cl = 0
for _ in range(int(input())):
    t, s, m = input().split()
    s = int(s)
    m = m_t(m)
    nw = m - cl
    if h>a:
        lh += nw
    elif a>h:
        la += nw
    if t == 'H':
        h += s
    elif t == 'A':
        a += s
    cl = m
nw = m_t('32:00') - cl
if h > a:
    lh += nw
elif a > h:
    la += nw
v = 'H'
if a > h:
    v = 'A'
print(v, t_m(lh), t_m(la))
l=['ee','ii','oo','aa','uu','yy']
n=int(input())
def co(h):
    cc=0
    for i in l:
        cc+=h.count(i)
    return cc
d={}
while(n!=0):
    for i in range(n):
        b=input()
        d[b]=co(b)
    kk=list(d.values())
    ll=list(d.keys())
    print(ll[kk.index(max(kk))])
    d={}
    n=int(input())

s='ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'*3
l=input().split()
while l[0]!='0':
    n=int(l[0])
    p=''
    for  i in l[1]:
        p+=s[s.index(i)+n]
    k=list(p)
    k.reverse()
    print(''.join(k))
    l=input().split()

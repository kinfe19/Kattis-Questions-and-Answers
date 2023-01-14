import string
b=string.ascii_lowercase
n=int(input())
for j in range(n):
    g=input().lower()
    l=[]
    for i in b:
        if i not in g:
            l.append(i.lower())
    l.sort()
    if len(l)==0:
        print('pangram')
    else:
        print('missing',''.join(l))

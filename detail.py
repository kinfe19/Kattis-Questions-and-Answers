n=int(input())
for i in range(n):
    l=[]
    h=input()
    g=input()
    p=True
    if(len(h)==len(g)):
        for j in range(len(h)):
            if not((h[j].isalpha() or h[j].isdigit())and(g[j].isalpha()or g[j].isdigit())):
                p=False
                break
    if(p):
        for k in range(len(h)):
            if(h[k]==g[k]):
                l.append('.')
            else:
                l.append('*')
    if(p and len(h)==len(g)):
        print(h)
        print(g)
        print(*l,sep='')
        

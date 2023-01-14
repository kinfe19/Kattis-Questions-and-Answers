a,b,c=input().split()
ls=[]
ls.append(int(a))
ls.append(int(b))
ls.append(int(c))
l=[]
for s in range(3):
    l.append(max(ls))
    ls.remove(max(ls))
g=input()
for i in g:
    if(i=='A'):
        ls.append(l[2])
    elif(i=='B'):
        ls.append(l[1])
    elif(i=='C'):
        ls.append(l[0])
print(*ls,sep=' ')

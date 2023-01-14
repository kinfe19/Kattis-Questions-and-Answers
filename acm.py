l=input().split()
d={}
c=0
t=0
while l[0]!='-1':
    if l[-1]=='right':
        c+=1
        try:
            t+=d[l[1]]*20+int(l[0])
            del(d[l[1]])
        except:
            t+=int(l[0])
    else:
        try:
            d[l[1]]+=1
        except:
            d[l[1]]=1
  
    l=input().split()

print(c,t)

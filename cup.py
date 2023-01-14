t=int(input())
d={}
l=[]
for i in range(t):
    j=input().split()
    if(j[0].isdigit()):
        j[0]=int(int(j[0])/2)
        d[j[0]]=j[1]
        l.append(j[0])
    else:
        d[int(j[1])]=j[0]
        l.append(int(j[1]))
l.sort()
for a in l:
    print(d[a])
    

g=int(input())
l=[]
k=[]
for i in range(g):
    p,m= input().split()
    n=1
    if(n<=12):
        if(not p in l):
            l.append(p)
            k.append(m)
            n+=1
for j in range(12):
    print(l[j]+" "+k[j])
        
    

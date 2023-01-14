d={'A':(11,11),'K':(4,4),'Q':(3,3),'J':(20,2),'T':(10,10),'9':(14,0),'8':(0,0),'7':(0,0)}
j,k=input().split()
j=4*int(j)
s=0
for i in range(j):
    n=input()
    if(n[1]==k):
        s+=d[n[0]][0]
    else:
        s+=d[n[0]][1]
print (s)

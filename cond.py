t=input()
s=int(len(t)/3)
k=0
for i in range(s):
    if(t[2*i+i]!='P'):
        k+=1
    if(t[2*i+i+1]!='E'):
        k+=1
    if(t[2*i+i+2]!='R'):
        k+=1
print(k)

f=input()
c=0
t=0
g=0
for i in f:
    if(i=='C'):
        c+=1
    elif(i=='G'):
        g+=1
    elif(i=='T'):
        t+=1
s=0
m=7*min(c,g,t)
s=c*c+t*t+g*g+m
print (s)

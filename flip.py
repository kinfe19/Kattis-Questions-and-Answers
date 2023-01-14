a,b=input().split()
a1=[]
b1=[]
for i in range(3):
    a1.append(int(a[-(i+1)]))
    b1.append(int(b[-(i+1)]))
a2=100*a1[0]+10*a1[1]+a1[2]
b2=100*b1[0]+10*b1[1]+b1[2]
if(a2>b2):
    print(a2)
elif(b2>a2):
    print(b2)

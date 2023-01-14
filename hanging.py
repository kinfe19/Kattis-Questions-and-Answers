g,m=input().split()
j=0
c=0
for i in range(int(m)):
    h,l=input().split()
    if(h=='enter'):
        if(int(l)+j>int(g)):
            c+=1
        else:
            j+=int(l)
    elif(h=='leave'):
        j-=int(l)
print(c)

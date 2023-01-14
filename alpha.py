st=input()
s=0.0
l=0.0
u=0.0
o=0.0
for i in st:
    if(i=='_'):
        s+=1
    elif(i.islower()):
        l+=1
    elif(i.isupper()):
        u+=1
    else:
        o+=1
print(s/len(st))
print(l/len(st))
print(u/len(st))
print(o/len(st))

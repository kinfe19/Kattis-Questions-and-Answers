p=input()
n=True
m=False
for i in p:
    if not(i.islower()):
        n=False
        break;
if(n):
    for i in range(len(p)-1):
        if(p[i]=='s' and p[i+1]=='s'):
            m=True
            break
if(m):
    print('hiss')
else:
    print('no hiss')

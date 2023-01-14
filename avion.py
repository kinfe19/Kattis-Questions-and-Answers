j=[]
for l in range(1,6):
    t=input()
    f=list(t)
    g=True
    for i in f:
        if not(i.isupper()or i.isdigit() or i=='-'):
            g=False
            break
    if(g ):
        if('FBI' in t):
            j.append(l)
if(len(j)==0):
    print('HE GOT AWAY!')
else:
    print(*j, sep = " ")

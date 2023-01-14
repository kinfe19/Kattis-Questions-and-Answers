j=input().split()
h=[]
p=True
for i in range(len(j)):
    if(j[i] not in h):
        h.append(j[i])
    else:
        p=False
        break
if(p):
    print('yes')
else:
    print('no')

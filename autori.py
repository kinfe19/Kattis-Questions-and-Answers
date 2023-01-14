t=input()
h=list(t)
j=[]
b=True
for i in h:
    if not(i.isalpha() or i=='-'):
        b=False
    if(i.isupper()):
        j.append(i)
l=''.join(j)
if(b):
    print(l)

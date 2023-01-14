c=int(input())
a=[]
for i in range (c):
    l=int(input())
    a.append(l)
h=a[-1]
if(len(a)==h):
    print('good job')
else:
    for j in range(1,h+1):
        if not(j in a):
            print(j)

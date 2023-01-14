n=int(input())
J=1
while(n!=0):
    print("SET",J)
    l=[input() for i in range(n)]
    i=0
    f=[]
    while(i<len(l)):
        print(l[i])
        f.append(l[i])
        i+=2
    for i in f:
        l.remove(i)
    l.reverse()
    for i in l:
        print(i)
    J+=1
    n=int(input())

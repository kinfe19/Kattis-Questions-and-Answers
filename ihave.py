n=int(input())
for i in range(n):
    o=[]
    j=int(input())
    for h in range(j):
        b=input()
        m=len(b)>=1
        n=True
        for i in b:
            if not(i.islower()):
                n=False
        if(n and m):
            if not (b in o):
                o.append(b)
    print(len(o))

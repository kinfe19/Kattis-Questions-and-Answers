i=1
while(1):
    try:
        a,b=[int(i) for i in input().split()]
        c,d=[int(i) for i in input().split()]
        v=input()
        f=a*d-c*b
        a//=f
        b//=f
        c//=f
        d//=f
        print("Case "+str(i)+':')
        print(d,-b)
        print(-c,a)
        i+=1
    except:
        break

while(1):
    try:
        a,b,c=[int (i) for i in input().split()]
        s=str(a//b)+"."
        for i in range(c):
            a=(a%b)*10
            s+=str(a//b)
        print(s)
    except:
        break

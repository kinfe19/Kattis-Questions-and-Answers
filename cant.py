d={}
while(1):
    try:
        g=input()
        h=g.split()
        d[h[1]]=h[0]
    except:
        break
while(1):
    try:
        n=input()
        if(n in d):
            print(d[n])
        elif(n!=''):
            print("eh")
    except:
        break

from math import *
while True:
    try:
        g=[]
        b=int(input())
        for i in range(1,int(sqrt(b))+1):
            if b%i==0 :
                g.append(i)
                if b//i not in g:
                    g.append(b//i)
        g.remove(b)
        if sum(g)==b:
            print(b,"perfect")
        elif abs(sum(g)-b)<=2:
            print(b,"almost perfect")
        else:
            print(b,"not perfect")
        l=g
    except:
        break


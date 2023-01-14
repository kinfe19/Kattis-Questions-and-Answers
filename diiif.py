from math import *
while True:
    try:
        t=input().split()
        if(t[0].isdigit()and t[1].isdigit()):
            a=int(t[0])
            b=int(t[1])
            print(abs(a-b))
    except:
        break

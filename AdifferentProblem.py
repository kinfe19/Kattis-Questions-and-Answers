from math import*
while True:
    try:
        x,y = [int(i) for i in input().split()]
        print(abs(y-x))
    except:
        break

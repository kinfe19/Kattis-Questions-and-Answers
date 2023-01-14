from math import factorial
while True:
    try:
        x = input()
        lx = len(x)
        d = []
        for i in x:
            if not i in d:
                d.append(i)
        a = 1
        for i in d:
            a = a * factorial(x.count(i))
        print(factorial(lx)//a)
    except:
        break
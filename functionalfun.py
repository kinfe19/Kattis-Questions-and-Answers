while 1:
    try:
        a=input().split()[1:]
        b=input().split()[1:]
        D=[];R=[]
        for i in range(int(input())):
            c,d = input().split('->')
            D.append(c);R.append(d)
        if len(D)!=len(set(D)):print('not a function')
        elif len(set(D))==len(D) and len(set(R))==len(b)and len(set(D))==len(set(R)):print('bijective')
        elif len(set(D))==len(set(R)):print('injective')
        elif len(set(R))==len(b):print('surjective')
        else:print('neither injective nor surjective')
    except:
        break
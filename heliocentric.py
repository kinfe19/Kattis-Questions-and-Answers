c = 1
while 1:
    try:
        e, m = [int(i) for i in input().split()]
        dy = 0
        while not(e==0 and m==0):
            e = (e+1)%365
            m = (m+1)%687
            dy+=1
     
        print(f'Case {c}: {dy}')

        c+=1
    except:
        break
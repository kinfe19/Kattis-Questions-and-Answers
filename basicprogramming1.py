_, k = [int(i) for i in input().split()]
n = [int(i) for i in input().split()]
if k==1:
    print(7)
    
elif k==2:
    if n[0] > n[1]:
        print('Bigger')
    elif n[0] == n[1]:
        print('Equal')
    else:
        print('Smaller')
        
elif k==3:
    l = sorted(n[:3])
    print(l[1])
    
elif k ==4:
    print(sum(n))
    
elif k==5:
    s = 0
    for i in n:
        if i%2==0:
            s+=i
    print(s)
    
elif k==6:
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in n:
        print(s[i%26], end='')
    print()
    
elif k==7:
    f = 1
    vis = [n[0]]
    i = n[0]
    ln = len(n)
    c = 0
    while 1:
        if i >= ln :
            f = 0
            break
        elif i == ln-1:
            f = 2
            break
        i = n[i]
        vis.append(i)
        c += 1
        if c > ln:
            break
    if f == 2:
        print('Done')
    elif f == 1:
        print('Cyclic')
    else:
        print('Out')









        

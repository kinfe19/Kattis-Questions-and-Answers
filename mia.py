a,b,c,d = [int(i)for i in input().split()]
while a+b+d+c !=0:
    if a>b:p1=str(a)+str(b)
    else:p1=str(b)+str(a)
    if c>d:p2=str(c)+str(d)
    else:p2=str(d)+str(c)
    if p1==p2:
        print('Tie.')
    elif p1=='21':
        print('Player 1 wins.')
    elif p2=='21':
        print('Player 2 wins.')
    elif p1[0]==p1[1] or p2[0]==p2[1]:
        k=1
        if p1[0]!=p1[1] and p2[0]==p2[1]:
            print('Player 2 wins.')
        elif p1[0]==p1[1] and p2[0]!=p2[1]:
            print('Player 1 wins.')
        else:
            if int(p2)-int(p1)>0:
                print('Player 2 wins.')
            else:
                print('Player 1 wins.')
    else:
        if int(p2)-int(p1)>0:
            print('Player 2 wins.')
        else:
            print('Player 1 wins.')
    a,b,c,d = [int(i)for i in input().split()]

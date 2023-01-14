from itertools import combinations as co


while 1:
    try:
        l = [int(i) for i in input().split()]

        p = sorted([max(i, j) - min(i,j) for i, j in co(l, 2)])

        if len(p) != len(set(p)):
            print('not a ruler')
        elif len(p) == max(l):
            print('perfect')
        else:
            k = []
            for i in range(1, max(l)+1):
                if i not in p:
                    k.append(i)
            print('missing', *k)
    except:
        break
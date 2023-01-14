input()
l = [int(i) for i in input().split()]
wn = 6
while wn:
    if wn in l and l.count(wn)==1:
        print(l.index(wn)+1)
        break
    else:
        wn -= 1
if wn == 0:
    print('none')
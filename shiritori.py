n = int(input())
vo = []
las = ''
d = {}
for i in range(n):
    n = input()
    try:
        b = d[n]
        v = 2
        if i%2==0:
            v = 1
        vo.append(v)
    except:
        if las !='' and las[-1]!=n[0]:
            v = 2
            if i%2==0:
                v = 1
            vo.append(v)
        d[n] = 1
    las = n
if vo==[]:
    print('Fair Game')
else:
    print(f'Player {vo[0]} lost')
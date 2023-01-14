s = input()
c=1
while s != 'END':
    pd = 0
    ld = []
    for i in s:
        if i == '.':
            pd += 1
        elif i == '*':
            ld.append(pd)
            pd = 0
    ld.append(pd)
    lnd = len(set(ld[1:-1]))
    ss = 'NOT EVEN'
    if lnd==1 or lnd == 0:
        ss = 'EVEN'
    print(f'{c} {ss}')
    c+=1
    
    s = input()
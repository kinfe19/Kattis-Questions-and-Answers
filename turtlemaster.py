l = [list(input()) for i in range(8)]
cmd = input()
dr = 3 # north 1 south 2 west 3 east 4
dd = [1, 'up', 'down', 'right', 'left']
pos = [7, 0]
l[7][0]='.'

f = 1
for c in cmd:
    if c == 'F':
        if dr == 1:
            pos[0] -= 1
        elif dr == 2:
            pos[0] += 1
        elif dr == 3:
            pos[1] += 1
        else:
            pos[1] -= 1
        try:
            v = l[pos[0]][pos[1]]
            if v == 'C' or v == 'I':
                f = 0
                break
        except:
            f = 0
            break
    elif c == 'R':
        if dr == 1:
            dr = 3
        elif dr == 2:
            dr = 4
        elif dr == 3:
            dr = 2
        else:
            dr = 1
    elif c == 'L':
        if dr == 1:
            dr = 4
        elif dr == 2:
            dr = 3
        elif dr == 3:
            dr = 1
        else:
            dr = 2
    elif c =='X':
        ps = pos.copy()
        if dr == 1:
            ps[0] -= 1
        elif dr == 2:
            ps[0] += 1
        elif dr == 3:
            ps[1] += 1
        else:
            ps[1] -= 1
        try:
            v = l[ps[0]][ps[1]]
            if v == 'I':
                l[ps[0]][ps[1]] = '.'
            else:
                f = 0
                break
        except:
            f = 0
            break
    #print(pos, dd[dr])
if f and l[pos[0]][pos[1]]=='D':
    print('Diamond!')
else:
    print('Bug!')
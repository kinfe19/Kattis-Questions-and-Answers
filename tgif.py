m = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
w = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

n, mm = input().split()
ww = input()
n = int(n)
s = sum(d[:m.index(mm)]) + n-1

if m.index(mm) > 1:
    if (w.index(ww)+s+1)%7 == 4 or (w.index(ww)+s)%7 == 4:
        print('not sure')
    else:
        print(':(')
elif mm=='NOV' and n==29:
    if (w.index(ww)+s)%7 == 4:
        print('not sure')
    else:
        print(':(')
else:
    if (w.index(ww)+s)%7 == 4:
        print('TGIF')
    else:
        print(':(')
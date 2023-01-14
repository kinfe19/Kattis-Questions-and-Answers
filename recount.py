d = {}
s = input()
while s!='***':
    try:
        d[s] += 1
    except:
        d[s] = 1
    s = input()
dd = sorted([(j, i) for i, j in d.items()],reverse=True)
if dd[0][0] == dd[1][0]:
    print('Runoff!')
else:
    print(dd[0][1])
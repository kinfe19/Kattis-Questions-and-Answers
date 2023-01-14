d={'P':13, 'K':13, 'H':13, 'T':13}
l=input()
t=1
for j in range(0, len(l)-1, 3):
    i = l[j:j+3]
    d[i[0]]-=1
    if l.count(i)>1:
        t=0
if t:print(d['P'], d['K'], d['H'],d['T'])
else:print('GRESKA')
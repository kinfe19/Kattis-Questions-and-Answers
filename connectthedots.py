l = []
d = {}
while 1:
    try:
        s = input()
        if s == "":
            p = list(sorted(d.items()))
            for i in range(len(p)-1):
                x1, y1 = p[i][1]
                x2, y2 = p[i+1][1]
                x, q = min(x1, x2), max(x1, x2)
                y, z = min(y1, y2), max(y1, y2)
                if x==q:
                    for o in range(y+1, z):
                        h = l[x][o]
                        if h=='|' or h=='+':
                            l[x][o] = '+'
                        elif not (h.isdigit() or h.isalpha()):
                            l[x][o] = '-'
                else:
                    for o in range(x+1, q):
                        h = l[o][y]
                        if h=='-'or h=='+':
                            l[o][y] = '+'
                        elif not (h.isdigit() or h.isalpha()):
                            l[o][y] = '|'

            for i in l:
                print(''.join(i))
            print()
            l = []
            d = {}
        else:
            for x, i in enumerate(s):
                if i.isdigit():
                    d[i] = [len(l), x]
                elif i.isalpha():
                    j = i
                    if j.isupper():
                        j = j.lower()
                    else:
                        j = j.upper()
                    d[j] = [len(l), x]
            l.append(list(s))
    except:
        break
p = list(sorted(d.items()))
for i in range(len(p)-1):
    x1, y1 = p[i][1]
    x2, y2 = p[i+1][1]
    x, q = min(x1, x2), max(x1, x2)
    y, z = min(y1, y2), max(y1, y2)
    if x==q:
        for o in range(y+1, z):
            h = l[x][o]
            if h=='|' or h=='+':
                l[x][o] = '+'
            elif not (h.isdigit() or h.isalpha()):
                l[x][o] = '-'
    else:
        for o in range(x+1, q):
            h = l[o][y]
            if h=='-' or h=='+':
                l[o][y] = '+'
            elif not (h.isdigit() or h.isalpha()):
                l[o][y] = '|'

for i in l:
    print(''.join(i))
print()

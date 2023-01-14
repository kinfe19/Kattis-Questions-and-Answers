v = 'aeiou'
s = []
for x in input().lower().split():
    i = 0
    ss = ''
    ln = len(x)
    while i<len(x):
        if x[i] in v:
            ss += x[i]
            i += 3
        else:
            ss+=x[i]
            i+=1
    s.append(ss)
print(*s)
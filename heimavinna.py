c = 0
for i in input().split(';'):
    b = i.split('-')
    if len(b) == 1:
        c += 1
    else:
        c += int(b[1]) - int(b[0]) + 1
print(c)
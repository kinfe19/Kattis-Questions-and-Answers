def countones(st):
    dc = {}
    for i in st:
        if i in dc:
            dc[i] += 1
        else:
            dc[i] = 1
    c = 0
    for i in dc.values():
        if i % 2 != 0:
            c += 1
    return max(0, c-1)
print(countones(input()))
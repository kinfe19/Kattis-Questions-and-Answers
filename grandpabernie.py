d = {}
for i in range(int(input())):
    s, v = input().split()
    v = int(v)
    try:
        d[s].append(v)
    except:
        d[s] = [v]
for i in d:
    d[i] = sorted(d[i])
for i in range(int(input())):
    s, v = input().split()
    print(d[s][int(v)-1])
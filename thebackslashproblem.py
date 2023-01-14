n = ord('!')
m = ord('*')
p = ord('[')
q = ord(']')
while True:
    try:
        x = int(input())
        s = list(input())
        for i in range(x):
            r = ""
            for j in s:
                v = ord(j)
                if (v >= n and v <= m) or (v >= p and v <= q):
                    r += "\\" + j
                elif j == '\\':
                    r += "\\\\"
                else:
                    r += j
            s = list(r)
        print(''.join(s))
    except:
        break
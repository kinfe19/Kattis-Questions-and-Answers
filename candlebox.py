lr = [0, 0, 0, 4]
lt = [0, 0, 3, 4]
d, r, t = [int(input()) for i in range(3)]
n = 4
while 1:
    p = r - sum(lr)
    m = sum(lt[:n-d])-t
    if m == p:
        print(m)
        break
    n += 1
    lr.append(n)
    lt.append(n)
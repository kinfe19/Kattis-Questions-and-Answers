for _ in range(int(input())):
    f = [int(j) for j in input()]
    for i in range(len(f)-1, -1, -1):
        if f[i] != 0:
            f[i]-=1
            break
    p = ''.join([str(i) for i in f])
    print(int(p))
    

for _ in range(int(input())):
    n, s = input().split()
    for i in range(int(n)):
        c = len(s) // 4
        s = s[c:][::-1]
        if c==0:
            break
    if i%2==0:
        s = s[::-1]
    print(s)
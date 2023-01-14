t = 1
m, n = sorted(map(int, input().split()))
if n == m or n%m ==0:
    print('win')
elif 2*m < n:
    print('win')
else:
    while True:
        if (n == 2 and m == 1):
            break
        if n == m or n%m ==0:
            if t%2 == 1:
                print('win')
            else:
                print('lose')
            break
        elif 2*m < n:
            if t%2 == 1:
                print('win')
            else:
                print('lose')
            break
        n = n - m
        x = m
        m = n
        n = x
        t += 1
    if n == 2 and m == 1:
        if t%2 == 1:
            print('win')
        else:
            print('lose')
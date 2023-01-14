def fn(n):
    return 1 if n==1 else 2*n - 2
def fn2(n):
    m =  n// 2
    return n + m*n - m*(m-1)*2
while 1:
    try:
        print(fn(int(input())))
    except:
        break
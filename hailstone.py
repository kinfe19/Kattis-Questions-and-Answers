def fn(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n +1
n = int(input())
sm = n
while n != 1:
    n = fn(n)
    sm += n
print(sm)
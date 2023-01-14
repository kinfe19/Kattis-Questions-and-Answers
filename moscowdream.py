a, b, c, n = [int(i)for i in input().split()]
if a>0 and b>0 and c>0 and n>3 and n <= a+b+c:
    print('YES')
else:
    print('NO')
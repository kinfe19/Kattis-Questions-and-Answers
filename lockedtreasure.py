from math import factorial as f
for i in range(int(input())):
    n, m = [int(i) for i in input().split()]
    m -= 1
    print(f(n) // (f(n-m) * f(m)))
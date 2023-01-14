from math import factorial as f,floor
h=int(input())
for i in range(h):
    n=int(input())
    print(f(2*n)//(f(n+1)*f(n)))

from math import gcd

# for _ in range(int(input()))

input()

x, *l = [int(i) for i in input().split()]
for i in l:
	y = x // gcd(x, i)
	z = i // gcd(x, i)
	print(str(y)+'/'+str(z))
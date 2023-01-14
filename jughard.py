from math import gcd
for _ in range(int(input())):
	a, b, c = map(int, input().split())
	print(['No', 'Yes'][c%gcd(a, b)==0])
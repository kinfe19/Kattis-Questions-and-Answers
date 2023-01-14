from itertools import combinations as com 
n = int(input())
l = [[int(i) for i in input().split()] for _ in range(n)]
mn = float('Inf')
for c in range(1, n+1):
	for j in com(range(n), c):
		p = 1 
		s = 0 
		for i in j:
			p *= l[i][0]
			s += l[i][1]
		x = abs(p - s)
		mn = min(x, mn)
print(mn)
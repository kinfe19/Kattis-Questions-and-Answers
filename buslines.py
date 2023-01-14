from itertools import combinations as com 
from pprint import pprint
n, m = map(int, input().split()) 
if m < n-1:
	print(-1)
else:
	d = []
	x = []
	c = 0
	for i in  com(range(1, n+1), 2):
		if sum(i) not in d:
			d.append(sum(i))
			x.append(i)
			c += 1
			if c == m:
				break
	if c < m:
		print(-1)
	else:
		for i, j in x:
			print(j, i)
from math import ceil
n, k = map(int, input().split())
i = 0
l = []
mx = 0
for j in range(n):
	x = int(input())
	l.append(x)
	while x - l[i] > 999:
		i += 1 
	mx = max(mx, j-i+1)
print(ceil(mx/k)) 
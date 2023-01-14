n, k = map(int, input().split())
m = [0 for i in range(k+1)]
l = sorted([[int(i) for i in input().split()]for _ in range(n)], reverse=True)
c = 0 
for i, j in l:
	if sum(m) == k+1:
		break 
	b = j 
	while 1:
		if b < 0:
			break
		if m[b] == 0:
			m[b] = 1
			c += i 
			break
		b -= 1
print(c)

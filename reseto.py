n, k = map(int, input().split())
l = [0 for i in range(n+1)]
l[1] = l[0] = 1
c = 0
p = 0
for i in range(2, n+1):

	if not l[i]:
		c += 1
		if c == k:
			p = i
			break
		#print(i,c, end='xx')
		for j in range(i+i, n+1, i):

			if not l[j]:
				c += 1
			#print(j,c, end='- ')
			l[j] = 1
			if c == k:
				p = j
				break
	if p:
		break 
print(p)

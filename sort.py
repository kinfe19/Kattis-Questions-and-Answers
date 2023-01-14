n, m = map(int, input().split())
l = [int(i) for i in input().split()]
fd = {}
od = {}
c = 0
for i in l:
	try:
		b = od[i]
	except:
		od[i] = c
		c += 1
	try:
		fd[i] += 1
	except:
		fd[i] = 1
s = [(-fd[i], od[i], i) for i in l]
print(*[i[2] for i in sorted(s, key=lambda x:(x[0], x[1], x[2]))])

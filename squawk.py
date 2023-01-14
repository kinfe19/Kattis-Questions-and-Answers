n, m, s, t = map(int, input().split())
d = [[] for i in range(n)]
for _ in range(m):
	a, b = map(int, input().split())
	d[a].append(b)
	d[b].append(a)
pr = [0 for i in range(n)]
pr[s] = 1
for _ in range(t):
	nw = [0 for i in range(n)]
	for i in range(n):
		if pr[i] != 0:
			x = pr[i]
			for j in d[i]:
				nw[j] += x
	pr = nw
print(sum(pr))

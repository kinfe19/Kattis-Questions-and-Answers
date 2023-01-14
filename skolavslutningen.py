n, k, m = map(int, input().split())
ss = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:m]
l = [[] for i in range(m)]
p = []
for j in range(n):
	p.append(list(input()))
for i in range(k):
	x = []
	for j in range(n):
		try:
			x.append(p[j][i])
		except IndexError:
			print(j, i)
	x = list(set(x))
	h = len(x)
	for j in range(h):
		for g in range(j+1, h):
			a, b = ss.index(x[j]), ss.index(x[g])
			if a not in l[b]:
				l[b].append(a)
			if b not in l[a]:
				l[a].append(b)
c = 0  
vis = [0 for i in range(m)]
for i in range(m):
	if vis[i] == 0:
		c += 1 
		st = [i]
		vis[i] = 1
		while st:
			s = st.pop()
			for j in l[s]:
				if vis[j] == 0:
					vis[j] = 1
					st.append(j)
print(c)
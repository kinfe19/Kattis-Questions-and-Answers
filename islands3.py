n, m = map(int, input().split())
l = []
for _ in range(n):
	s = input()
	l.append(list(s))
d = {}
for i in range(n):
	for j in range(m):
		x = l[i][j]
		if x == 'L' or x == 'C':
			d[(i, j)] = []
			if i+1<n and (l[i+1][j] == 'L' or l[i+1][j] == 'C'):
				d[(i, j)].append((i+1, j))
			if i>0 and (l[i-1][j] == 'L' or l[i-1][j] == 'C'):
				d[(i, j)].append((i-1, j))
			if j+1<m and (l[i][j+1] == 'L' or l[i][j+1] == 'C'):
				d[(i, j)].append((i, j+1))
			if j>0 and (l[i][j-1] == 'L' or l[i][j-1] == 'C'):
				d[(i, j)].append((i, j-1))
vis = {i:0 for i in d}
c = 0 
for i in d:
	x, y = i 
	if vis[i] == 0 and l[x][y] == 'L':
		c += 1 
		st = [i]
		vis[i] = 1 
		while st:
			s = st.pop()
			for j in d[s]:
				if vis[j] == 0:
					vis[j] = 1 
					st.append(j) 
print(c)
n, m = map(int, input().split())
d = {i+1:[] for i in range(n)}
visited = [0 for _ in range(n)]
for _ in range(m):
	x, y = map(int, input().split())
	d[x].append(y)
	d[y].append(x)
st = [1]
while st != []:
	s = st[-1]
	st.pop()
	visited[s-1] = 1
	for _ in d[s]:
		if not visited[_-1]:
			st.append(_)
#print(d, visited)
if sum(visited) == len(visited):
	print('Connected')
else:	
	for i, _ in enumerate(visited):
		if not _:
			print(i+1)
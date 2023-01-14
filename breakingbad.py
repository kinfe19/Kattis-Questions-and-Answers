d = {}
n = int(input())
for i in range(n):
	d[input()] = []
for i in range(int(input())):
	a, b = input().split()
	d[a].append(b)
	d[b].append(a)
f = True
vis = {i:-1 for i in d}
for i in d:
	if vis[i] == -1:
		st = [i]
		vis[i] = 0 
		while st:
			s = st.pop()
			for j in d[s]:
				if vis[j] == vis[s]:
					f = False
					break
				if vis[j] == -1:
					vis[j] = int(not vis[s])
					st.append(j)

if f:
	for i in vis:
		if vis[i] == 0:
			print(i, end=' ')
	print()
	for i in vis:
		if vis[i] == 1:
			print(i, end=' ')
	print()
else:
	print('impossible')
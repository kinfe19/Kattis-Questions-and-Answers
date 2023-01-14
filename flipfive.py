def child(s, i, j):
	k = [list(_) for _ in s]
	k[i][j] = int(not k[i][j])
	if i > 0:
		k[i-1][j] = int(not k[i-1][j])
	if j > 0:
		k[i][j-1] = int(not k[i][j-1])
	if i < 2:
		k[i+1][j] = int(not k[i+1][j])
	if j < 2:
		k[i][j+1] = int(not k[i][j+1])	 
	return tuple(tuple(_) for _ in k)

d = {((0, 0, 0), (0, 0, 0), (0, 0, 0)):[]}
p = [((0, 0, 0), (0, 0, 0), (0, 0, 0))]
while p:
	s = p.pop()
	for i in range(3):
		for j in range(3):
			k = child(s, i, j)
			d[s].append(k)
			if k not in d:
				p.append(k)
				d[k] = []
# from pprint import pprint
# pprint(d)
vis = {i:-1 for i in d}
st = [((0, 0, 0), (0, 0, 0), (0, 0, 0))]
vis[((0, 0, 0), (0, 0, 0), (0, 0, 0))] = 0 
while st:
	s = st.pop(0)
	for j in d[s]:
		if vis[j] == -1:
			vis[j] = vis[s] + 1 
			st.append(j)
# pprint(vis)

for _ in range(int(input())):
	f = []
	for i in range(3):
		o = []
		for j in input():
			if j == '*':
				o.append(1)
			else:
				o.append(0)
		f.append(tuple(o))
	print(vis[tuple(f)])

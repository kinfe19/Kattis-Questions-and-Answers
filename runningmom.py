
n = int(input())
d = {}
for _ in range(n):
	a, b = input().split()
	try:
		d[a].append(b)
	except:
		d[a] = [b]
	if d.get(b) == None:
		d[b] = []
ln = len(d)
while 1:
	try:
		x = input()
		f = 0 
		st = [x]
		# vis = {i:0 for i in d}
		while st != []:
			s = st.pop()
			# vis[s] = 1
			for _ in d[s]:
				if len(st) > n:
					f = 1
					break
				st.append(_)
			if f:
				break
		if f:
			print(x, 'safe')
		else:
			print(x, 'trapped')
	except Exception as e:
		#print(e)
		break

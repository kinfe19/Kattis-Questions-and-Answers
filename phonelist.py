
for _ in range(int(input())):
	d = {}
	g = {}
	f = True
	for __ in range(int(input())):
		s = input()
		if g.get(s) != None:
			f = False
		if f:
			x = ''
			for i in s:
				x += i
				g[x] = 1 
				if d.get(x) != None:
					f = False 
					break 
			d[s] = 1 
	if f:
		print('YES')
	else:
		print('NO')
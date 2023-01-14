l = ['..#..', '.#.#.' ,'#.X.#', '.#.#.', '..#..']
p = [list(i.replace('#', '*')) for i in l]
l = [list(i) for i in l]
k = [l, l, p]

s = input()
ln = len(s)-1
for i in range(5):
	t = ''
	for j in range(ln):
		x = k[j%3][i][:-1]
		if i == 2:
			x[2] = s[j]
			if j % 3 == 0 and j != 0:
				x[0] = '*'
		t += ''.join(x)
	x = k[ln%3][i]
	if i == 2:
		x[2] = s[ln]
		if ln % 3 == 0 and ln != 0:
			x[0] = '*'
	t += ''.join(x)
	print(t)

def max_pos(l, pi, pj, ds, org, w):
	f = 1
	for i, j in l:
		if abs(pi-i) == abs(pj-j) == 1:
			if pi > i and pj > j:
				if pi > 1 and pj > 1 and (pi-2, pj-2) not in l and (pi-2, pj-2) not in w:
					k = l.copy()
					k.remove((i, j))
					max_pos(k, pi-2, pj-2, ds+1, org, w)
					f = 0
			elif pi > i and pj < j:
				if pi > 1 and pj < 8 and (pi-2, pj+2) not in l and (pi-2, pj+2) not in w:
					k = l.copy()
					k.remove((i, j))
					max_pos(k, pi-2, pj+2, ds+1, org, w)
					f = 0
			elif pi < i and pj > j:
				if pi < 8 and pj > 1 and (pi+2, pj-2) not in l and (pi+2, pj-2) not in w:
					k = l.copy()
					k.remove((i, j))
					max_pos(k, pi+2, pj-2, ds+1, org, w)
					f = 0
			elif pi < i and pj < j:
				if pi < 8 and pj < 8 and (pi+2, pj+2) not in l and (pi+2, pj+2) not in w:
					k = l.copy()
					k.remove((i, j))
					max_pos(k, pi+2, pj+2, ds+1, org, w)
					f = 0
	if f or l == []:
		org.append(ds)
		return 

for _ in range(int(input())):
	input()
	w = []
	b = []
	for i in range(10):
		s = input()
		for j in range(10):
			if s[j] == 'W':
				w.append((i, j))
			elif s[j] == 'B':
				b.append((i, j))
	# print(w)
	
	mx = 0
	for i, j in w:
		wk = w.copy()
		wk.remove((i, j))
		org = [0]
		max_pos(b, i, j, 0, org, wk)
		mx = max(max(org), mx)
	print(mx)

for _ in range(int(input())):
	p, k, n = map(int, input().split())
	l = sorted([int(i) for i in input().split()])
	i = 0
	x = 1
	s = 0
	f = True
	# print(l)
	while l:
		s += x*l[-1]
		# print(s, end=' ')
		l.pop()
		i += 1 
		if i == k:
			x += 1 
			i = 0
			if x == p:
				f = False
	# print()
	print(f'Case #{_+1}: {s}')
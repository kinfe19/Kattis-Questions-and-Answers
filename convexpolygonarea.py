for _ in range(int(input())):
	n, *l = [int(i) for i in input().split()]
	x = [l[2*i] for i in range(n)]
	y = [l[2*i+1] for i in range(n)]
	x += [x[0]]
	y += [y[0]]
	s = 0
	m = 0
	for i in range(n):
		s += x[i]*y[i+1]-y[i]*x[i+1]

	print(abs(s/2))

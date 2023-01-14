def con(s):
	a, b = s.split()
	x, y = [int(i) for i in a.split(':')]
	return x%12 + y/60 + [12, 0][b=='a.m.']

while 1:
	t = int(input())
	if t == 0:
		break
	for i, j in  sorted(map(lambda x:(con(x), x), [input() for _ in range(t)])):
		print(j)
	print()
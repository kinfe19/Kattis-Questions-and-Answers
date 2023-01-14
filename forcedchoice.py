n, s, m = map(int, input().split())
for _ in range(m):
	if s in [int(i) for i in input().split()][1:]:
		print('KEEP')
	else:
		print('REMOVE')
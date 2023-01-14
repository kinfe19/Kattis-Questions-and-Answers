n, q = map(int, input().split())
l = [int(_) for  _ in input().split()]
for _ in range(q):
	a, b, c = map(int, input().split())
	if a == 1:
		l[b-1] = c 
	else:
		print(abs(l[b-1]-l[c-1]))
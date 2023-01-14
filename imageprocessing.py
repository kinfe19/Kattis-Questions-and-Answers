
def conv(a, b, x, y, n, m):
	p = [[0 for _ in range(y-m+1)]for __ in range(x-n+1)]
	for i in range(x-n+1):
		for j in range(y-m+1):
			sm = 0
			for k in range(n):
				for l in range(m):
					sm += a[k+i][l+j] * b[n-k-1][m-l-1]
			p[i][j] = sm 
	return p
x, y, n, m = map(int, input().split())
a = [[int(_) for _ in input().split()] for __ in range(x)]
b = [[int(_) for _ in input().split()] for __ in range(n)]
for i in conv(a, b, x, y, n, m):
	print(*i)
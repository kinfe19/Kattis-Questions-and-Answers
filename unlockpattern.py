l = [[int(i) for i in input().split()] for _ in range(3)]
def x(n):
	for i in range(3):
		for j in range(3):
			if n == l[i][j]:
				return (i, j)
def ds(a, b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5
d = 0
for _ in range(2, 10):
	d += ds(x(_), x(_-1))
print(d)
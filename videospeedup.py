n, p, k = map(int, input().split())
l = [0] + [int(_) for _ in input().split()] + [k]
y = 1
s = 0
for i in range(n+1):
	s += (l[i+1]-l[i])*y
	y += p / 100
print('%.6f'%s)
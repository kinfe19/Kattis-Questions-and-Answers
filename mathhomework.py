a, b, c, d = map(int, input().split())
f = 1
for i in range(d//a+1):
	for j in range(d//b+1):
		for k in range(d//c+1):
			if a*i+b*j+c*k == d:
				print(i, j, k)
				f = 0
if f:
	print('impossible')


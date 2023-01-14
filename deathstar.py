n = int(input())
p = [list('x'*30) for i in range(n)]
l = [[bin(int(i))[2:] for i in input().split()]for _ in range(n)]
for i in range(n):
	for j in range(i+1, n):
		x = l[i][j]
		for k in range(len(x)):
			if x[-(k+1)] == '1':
				p[i][-(k+1)] = '1'
				p[j][-(k+1)] = '1'
for i in p:
	print(int(''.join(i).replace('x', '0'), 2), end=' ')
print()
n = int(input())
l = [int(input()) for _ in range(n)]

if n % 2:
	print('still running')
else:
	print(sum([l[i*2+1]-l[i*2] for i in range(n//2)]))
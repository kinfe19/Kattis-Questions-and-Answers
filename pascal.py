from math import ceil
n = int(input())
for i in range(2, int(n**.5)+1):
	if n % i == 0:
		print(n-n//i)
		break
else:
	print(n-1)

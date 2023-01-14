n = int(input())
l = sorted([int(i) for i in input().split()])
f = False
for i in range(n-2):
	a, b, c = l[i], l[i+1], l[i+2]
	if a+b > c:
		f = True 
		break
print(['impossible', 'possible'][f])


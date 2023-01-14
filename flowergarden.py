def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(n**.5)+1):
		if n % i == 0:
			return False 
	return True
def ds(a, b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5
for _ in range(int(input())):
	a, b = map(int, input().split())
	c = 0
	pr = 0
	px = 0
	py = 0
	f = 1
	d = 0
	for j in range(a):
		x, y = map(int, input().split())
		if f:
			d += ds((px, py), (x, y))
			if d > b:
				f = 0
			else:
				c += 1
				if is_prime(c):
					pr = c
		px = x
		py = y 
	print(pr)
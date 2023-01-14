def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

while 1:
	a, b = map(int, input().split())
	if a + b == 0:
		break
	for _ in range(b):
		x, o, y = input().split()
		x, y = int(x), int(y)
		if o=='/':
			k = modinv(y, a)
			if k == -1:
				print(-1)
			else:
				print(k*x%a)
		else:
			print(eval(str(x%a)+o+str(y%a))%a)

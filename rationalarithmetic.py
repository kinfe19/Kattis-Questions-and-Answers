from math import gcd
def lcm(a, b):
	return a*b//gcd(a, b)
def prin(a, b):
	if b < 0 :
		a = -a
		b = -b 	 
	print(a, '/', b)

for _ in range(int(input())):
	a, b, o, c, d = input().split()
	a, b, c, d = map(int, [a, b, c, d])
	if o == '/':
		x = a*d 
		y = b*c
		prin(x//gcd(x, y), y//gcd(x, y))
	elif o == '*':
		x = a*c 
		y = b*d 
		prin(x//gcd(x, y), y//gcd(x, y))
	else:
		g = lcm(b, d)
		n = eval(str(a*g//b)+o+str(c*g//d))
		prin(n//gcd(n, g),  g//gcd(n, g))

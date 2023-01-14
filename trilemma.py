from math import pi, acos
def con(a, b, c, d, e, f):
	try:
		return (d-b) / (c-a) == (f-d) / (e-c)
	except:
		return False
def dis(x1, y1, x2 ,y2):
	return ((x1-x2)**2+(y1-y2)**2)**.5 
def form(a):
	k = str(a)
	x, y = k.split('.')
	if y.startswith('000000'):
		return int(x)
	if y.startswith('999999'):
		return int(x) +1
	else:
		return a
def ang(a, b, c):
	return form(acos((a**2+b**2-c**2)/(2*a*b))* 180 / pi)
for i in range(1, int(input())+1):
	a, b, c, d, e, f = map(int, input().split())	
	if a == c and c == e or b == d and d == f :
		print(f"Case #{i}: not a triangle")	
	elif con(a, b, c, d, e, f):
		print(f"Case #{i}: not a triangle")	
	else:
		try:
			s = f"Case #{i}: "
			x, y, z = dis(a, b, c, d), dis(c, d, e, f), dis(e, f, a, b)
			l, m, n = ang(x, y, z), ang(z, x, y), ang(y, z, x)
			if z == y and y == z and x == z:
				s += 'equilateral '
			elif x == y or y == z or x == z:
				s += 'isosceles '
			else:
				s += 'scalene '
			if l > 90 or m > 90 or n > 90:
				s += 'obtuse triangle'
			elif l == 90 or m == 90 or n == 90:
				s += 'right triangle'
			else:
				s += 'acute triangle'
			print(s)
		except:
			print(f"Case #{i}: not a triangle")
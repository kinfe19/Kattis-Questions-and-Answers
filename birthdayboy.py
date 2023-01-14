
def pr(a, b):
	a, b = map(str, [a, b])
	if len(a) == 1:
		a = '0'+a
	if len(b) == 1:
		b = '0'+b
	print(a+'-'+b)
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = int(input())
l = [[int(i) for i in input().split()[1].split('-')] for _ in range(n)]
a, b = min(l)
a -= 1
sp = 0 
f = []
mx = 0
st = [a+1, b]
for i in range(sum(m)): 
	sp += 1
	xx, yy = a, b
	if b+1 > m[a]:
		b = 1
		a += 1
		if a == 12:
			a = 0 
	else:
		b += 1
	if [a+1, b] in l:
		# print(st, [a+1, b], sp)
		if sp > mx:
			mx = sp 
			f = [[xx+1, yy]]
		elif sp == mx:
			f.append([xx+1, yy]	)
		st = [a+1, b]
		sp = 0 
if len(f) == 1:
	pr(*f[0])
else:
	g = []
	mn= sum(m)
	x, y = 9, 27
	for a, b in f:
		a -= 1
		ds = None
		if a < x:
			ds = 5+sum(m[10:])+sum(m[:a])+b
		elif a > x:
			ds = 27+sum(m[10:a])+b
		else:
			if b <= y:
				ds = sum(m)-(y-b)
			else:
				ds = b-y
		if ds < mn:
			mn = ds 
			g = [a+1, b]
		# print([a+1, b], ds)
	pr(*g)
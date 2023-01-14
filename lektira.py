def rev(s):
	l = list(s)
	n = len(s)
	for i in range(n//2):
		l[i], l[n-i-1] = l[n-i-1], l[i]
	return ''.join(l)
s = input()
n = len(s)
p = None
for i in range(1, n-1):
	for j in range(i+1, n):
		a, b, c = map(rev, [s[:i], s[i:j], s[j:]])
		x = a+b+c
		if p == None:
			p = x
		else:
			if x < p:
				p = x 
print(p)
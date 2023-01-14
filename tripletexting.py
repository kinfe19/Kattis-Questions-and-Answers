s = input()
ln = len(s)
a, b, c = s[:ln//3], s[ln//3:ln//3*2], s[ln//3*2:]
p = ''
for i in range(ln//3):
	x = a[i]+b[i]+c[i]
	for j in x:
		if x.count(j) >= 2:
			p+=j
			break
print(p)
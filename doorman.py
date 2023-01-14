n = int(input())
a = b = c = 0
l = list(input())
ln = len(l)
for i in range(ln):
	if l[i] == 'W':
		a += 1 
	else:
		b += 1 
	if abs(a-b) > n:
		if i+1 < ln and l[i+1] != l[i]:
			if l[i] == 'W':
				a -= 1
				b += 1
				l[i+1] = 'W'
			else:
				a += 1 
				b -= 1  
				l[i+1] = 'M'
		else:
			break 
	c += 1 
print(c)
n = input()
while len(n) > 1:
	p = 1
	for i in n:
		if i != '0':
			p *= int(i)
	n = str(p)
print(n)
p = input()
s = input()

if s == p or (s == p[:-1] and p[-1].isdigit()) or (s == p[1:] and p[0].isdigit()):
	print('Yes')
else:
	g = ''
	for i in p:
		if i.isalpha():
			if i.islower():
				g += i.upper()
			else:
				g += i.lower() 
		else:
			g += i 
	if g == s:
		print('Yes')
	else:
		print('No')

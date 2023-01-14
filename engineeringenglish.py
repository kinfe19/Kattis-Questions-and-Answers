
d = {}
while 1:
	try:
		s = input().split()
		for i in range(len(s)):
			if d.get(s[i].lower()) != None:
				s[i] = '.'
			else:
				d[s[i].lower()] = 1
		print(' '.join(s))
	except EOFError:
		break 

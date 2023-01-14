def sep(s):
	p = ''
	l = []
	for _ in s:
		if _.isalpha():
			p += _ 
		else:
			if p != '':
				l.append(p.lower())
				p = ''
	if p!= '':
		l.append(p.lower())
	return l
	
while 1:
	try:
		t = int(input())
		d = {}
		while 1:
			s = input()
			if s == 'EndOfText':
				break
			for _ in sep(s):
				try:
					d[_] += 1
				except:
					d[_] = 1
		k = []
		for i in d:
			if d[i] == t:
				k.append(i)
		if k == []:
			print('There is no such word.')
		else:
			for _ in sorted(k):
				print(_)
		print()
	except:
		break
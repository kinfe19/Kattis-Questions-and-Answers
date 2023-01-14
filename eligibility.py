for _ in range(int(input())):
	s, l, p, d = input().split()
	o = ''
	if int(l.split('/')[0]) >= 2010 or int(p.split('/')[0]) >= 1991:
		print(s, 'eligible')
	elif int(d) > 40:
		print(s, 'ineligible')
	else:
		print(s, 'coach petitions')
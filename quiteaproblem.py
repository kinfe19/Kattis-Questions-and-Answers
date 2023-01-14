while 1:
	try:
		s = input()
		print(['no', 'yes']['problem' in s.lower()])
	except EOFError:
		break

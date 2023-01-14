while 1:
	try:
		st = 1
		ss = []
		qu = 1
		qq = []
		pr = 1 
		pp = [] 
		f = 1 
		l = []
		for _ in range(int(input())):
			a, b = map(int, input().split())
			if a == 1:
				ss.append(b)
				qq.append(b)
				pp.append(b)
			else:
				if st and ss:
					if ss[-1] != b:
						st = 0 
					else:
						ss.pop()
				else:
					st = 0 
				if qu and qq:
					if qq[0] != b:
						qu = 0
					else: 
						qq.pop(0)
				else:
					qu = 0 
				if pr and pp:
					if max(pp) != b:
						pr = 0 
					else:
						pp.remove(b)
				else:
					pr = 0
		if sum([st, qu, pr]) > 1:
			print('not sure')
		elif st:
			print('stack')
		elif qu:
			print('queue')
		elif pr:
			print('priority queue')
		else:
			print('impossible')
	except EOFError:
		break
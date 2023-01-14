for _ in range(int(input())):
	l = input().split()
	p = []
	while 1:
		s = input()
		if s == "what does the fox say?":
			break 
		p.append(s.split()[-1])
	for i in l:
		if i not in p:
			print(i, end=' ')
	print()
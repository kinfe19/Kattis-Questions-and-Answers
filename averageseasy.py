for _  in range(int(input())):
	input()
	c, e = map(int, input().split())
	cc = [int(i) for i in input().split()]
	sc = sum(cc)
	ac = sc / c
	ee = [int(i) for i in input().split()]
	se = sum(ee)
	ae = se / e
	s = 0
	for i in cc:
		aen = (se + i) / (e + 1)
		acn = (sc - i) / (c - 1)
		if aen > ae and acn > ac:
			s += 1
	print(s)
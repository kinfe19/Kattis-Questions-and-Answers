
for _ in range(int(input())):
	s = input()
	a = int(s[:3])
	s = int(s)
	ds = float("Inf")
	n = []
	if a - 1 >= 100:
		x = int(str(a-1)+str(a-1)[::-1])
		k = abs(s-x)
		if k == ds:
			n.append(x)
		elif k < ds:
			ds = k
			n = [x]
	if a + 1 < 1000:
		x = int(str(a+1)+str(a+1)[::-1])
		k = abs(s-x)
		if k == ds:
			n.append(x)
		elif k < ds:
			ds = k
			n = [x]
	x = int(str(a)+str(a)[::-1])
	k = abs(s-x)
	if k == ds:
		n.append(x)
	elif k < ds:
		ds = k
		n = [x]
	print(min(n))

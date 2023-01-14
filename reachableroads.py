for __ in range(int(input())):
	n = int(input())
	d = {i:[] for i in range(n)}
	vist = [1 for i in range(n)]
	dis = 0
	for _ in range(int(input())):
		a, b = map(int, input().split())
		d[a].append(b)
		d[b].append(a)
	for _ in d:
		if vist[_]:
			st = [_]
			while st != []:
				s = st[-1]
				st.pop()
				vist[s] = 0
				for __ in d[s]:
					if vist[__]:
						st.append(__)
			dis += 1
	print(max(dis-1, 0))
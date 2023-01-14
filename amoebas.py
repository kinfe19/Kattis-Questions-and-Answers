def dr8(i, j):
	return [(i-1, j), (i, j-1), (i+1, j), (i, j+1), (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1)]
a, b = map(int, input().split())
h = []

for i in range(a):
	for j, _ in enumerate(input()):
		if _== '#':
			h.append((i, j))
c = 0
while h != []:
	st = [h[0]]
	c += 1
	while st != []:
		s = st[-1]
		try:
			h.remove(s)
		except:
			pass
		st.pop()
		for i in dr8(*s):
			if i in h:
				st.append(i)
print(c)
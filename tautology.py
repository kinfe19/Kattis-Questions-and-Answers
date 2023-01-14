from itertools import permutations as com 
x = 'pqrst'
y = 'KANCE'
def cal(s, d):
	st = []
	for i in s[::-1]:
		if i in x:
			st.append(d[i])
		elif i in y:
			if i == 'N': # NOT
				s = st.pop()
				st.append(int(not s))
			elif i == 'K': # AND 
				a, b = st.pop(), st.pop()
				if a == 0 or b == 0:
					st.append(0)
				else:
					st.append(1)
			elif i == 'A': # OR
				a, b = st.pop(), st.pop()
				if a or b:
					st.append(1)
				else:
					st.append(0)
			elif i == 'C': # implication
				a, b = st.pop(), st.pop()
				if a == 1 and b == 0:
					st.append(0)
				else:
					st.append(1)
			elif i == 'E': #BI-implication
				a, b = st.pop(), st.pop()
				if a == b:
					st.append(1)
				else:
					st.append(0)
	return st.pop()

while 1:
	s = input()
	if s == '0':
		break 
	p = []
	for i in s:
		if i in x:
			p.append(i)
	p = list(set(p))
	f = True
	nn = len(p)
	for i in set(list(com([0]*nn+[1]*nn, len(p)))):
		d = {}
		for j in range(len(p)):
			d[p[j]] = i[j]
		ff = bool(cal(s, d))
		if not ff:
			f = False
	if f:
		print('tautology')
	else:
		print('not')
def ser(l):
	return sum(l)
def par(l):
	return 1 / sum([1 / i for i in l if i !=0])
d = {}
n = int(input())
l = [float(_) for _ in input().split()]
for i in range(n):
	d[f'{i+1}'] = l[i]
s = input()			
st = []
n = len(s)
for j in range(n):
	i = s[j]
	if i == ')':
		while len(st)>1 and st[-2] != '(':
			a, o, b = [st.pop() for _ in range(3)]
			if o == '-':
				st.append(ser([a, b]))
			elif o == '|':
				st.append(par([a, b]))
		st.pop(-2)
	elif i == '-' or i == '|' or i == '(':
		st.append(i)
	elif i == 'R':
		j += 1
		x = ''
		while j<n and s[j].isdigit():
			x += s[j]
			j += 1
		st.append(d[x])
if len(st) > 1:
	a, o, b = [st.pop() for _ in range(3)]
	if o == '-':
		st.append(ser([a, b]))
	elif o == '|':
		st.append(par([a, b]))
print('%.5f'%st[0])

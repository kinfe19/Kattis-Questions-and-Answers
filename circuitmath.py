def cal(a, op, b=None):
	if op == '+':
		if a == 'F' and b == 'F':
			return 'F'
		else:
			return 'T'
	elif op == '*':
		if a == 'T' and b == 'T':
			return 'T'
		else:
			return 'F'
	elif op == '-':
		return ['F', 'T'][a=='F']
n = int(input())
d = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n], input().split()))
p = input().split()
kk = ['*', '+', '-']
st = []
for i in p:
	if i in kk:
		if i == '-':
			st.append(cal(st.pop(-1), i))
		else:
			x, y = [st.pop(-1) for _ in range(2)]
			st.append(cal(x, i, y))
	else:
		st.append(d[i])
print(*st)
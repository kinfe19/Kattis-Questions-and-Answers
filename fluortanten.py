n = int(input())
l = [0]
p = [0]
c = 1
for j in input().split():
	if j != '0':
		l.append((c)*int(j))
		p.append((c+1)*int(j))
		c += 1
bb = sum(p)
ss = 0
mx = None
for i in range(n):
	bb -= p[i]
	ss += l[i]
	if mx == None or ss+bb > mx:
		mx = ss+bb
print(mx)

d = {}
u = {}
t = {}
for _ in range(int(input())):
	s, *p = input().split()
	if d.get(s) == None:
		d[s] = {}
	for i in p:
		if d[s].get(i) == None:
			u[i] = u.get(i, 0)+1
			d[s][i] = 1
		t[i] = t.get(i,0)+1
x = []
n = len(d)
for i in u:
	if u[i] == n:
		x.append([-t[i], i])
if x == []:
	print('ALL CLEAR')
else:
	x.sort()
	for _, i in x:
		print(i)
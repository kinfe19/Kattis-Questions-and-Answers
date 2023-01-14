f = 0
from math import ceil
while 1:
	n = int(input())
	if n == 0:
		break
	if f:
		print()
	l = []
	mx = 0 
	for _ in range(n):
		x = eval(input())
		l.append(x)
		mx = max(len(str(x)), mx)
	c = 1 
	ln = mx
	while 1:
		if ln + mx+1 > 50:
			break
		ln += mx+1
		c += 1
	for i in range(n):
		x = str(l[i])
		l[i] = ' '*(mx-len(x))+x
	for i in range(ceil(n/c)):
		print(*l[i*c:(i+1)*c])
	f = 1
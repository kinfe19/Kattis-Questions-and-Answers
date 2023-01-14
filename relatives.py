def seive(n):
	l = [1 for i in range(n+1)]
	l[0] = l[1] = 0
	for i in range(2, int(n**.5)+1):
		if l[i]:
			for j in range(i+i, n+1, i):
				l[j] = 0
	return [k for k, j in enumerate(l) if j]
l = seive(32000)
def prime_factors(k):
	d = {}
	i = 0
	while 1:
		if i >= 3432:
			d[k] = 1
			break
		elif l[i] > k:
			break
		elif k % l[i] == 0:
			d[l[i]] = 1
			k //= l[i]
		else:
			i += 1
	return d
# print(l[:20])
while 1:
	n = int(input())
	if n == 0:
		break
	s = prime_factors(n)
	for i in s:
		n *= (1-1.0/i) 
	print(int(n))
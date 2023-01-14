def check(l, n):
    p = [0 for i in range(n)]
    for i in range(n):
    	p[l[i]] = i 
    for i in range(n-2):
        for j in range(i+1, n):
        	k = 2*j - i
        	if k >= n:
        		break
        	if (p[i] > p[j] and p[j] > p[k]) or (p[k]>p[j] and p[j]>p[i]):
        		return False 
    return True 

while True:
    s = input()
    if s == '0':
        break 
    n, l = s.split(':')
    print(['no', 'yes'][check(list(map(int, l.split())), int(n))])

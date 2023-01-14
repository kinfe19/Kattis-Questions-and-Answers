n = int(input())
l = [int(input()) for i in range(n)]
k = sum(l)
s = 0 
mx = 0 
for i in range(n):
	s += l[i]**2 
	k -= l[i]
	mx = max(s*k, mx)
print(mx)

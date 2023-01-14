p, t = map(int, input().split())
x = 0
for i in range(p):
	f = 1
	for j in range(t):
		s = input()
		k = s[0].lower()+s[1:]
		if k != s.lower():
			f = 0 
	if f :
		x += 1
print(x)
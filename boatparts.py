p, n = map(int, input().split())
l = set()
x = None
for _ in range(n):
	l.add(input())
	if len(l) == p and x == None:
		x = _+1 
print('paradox avoided' if x == None else x)
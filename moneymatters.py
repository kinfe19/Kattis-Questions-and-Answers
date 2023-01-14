n, t = map(int, input().split())

d = {i:[] for i in range(n)}
m = [int(input()) for _ in range(n)]
v = [0 for _ in range(n)]
for _ in range(t):
    a, b = map(int, input().split())
    d[a].append(b) 
    d[b].append(a)

f = 1
for _ in d:
    if not v[_]:
    	val = []
    	st = [_]
    	while st != []:
    		s = st[-1]
    		val.append(s)
    		st.pop()
    		v[s] = 1
    		for __ in d[s]:
    			if not v[__]:
    				st.append(__)
    	sm = 0 
    	for i in set(val):
    		sm += m[i]
    	if sm != 0:
    		f = 0
    		break
if f:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')

t = int(input())
mx = 0
l = [[int(i) for i in input().split()] for _ in range(t)]
for _ in range(1, t):
	for __ in range(_):
		k = (l[_][1]-l[__][1]) / (l[_][0]-l[__][0])
		if k > mx:
			mx = k
	
print(int(mx))

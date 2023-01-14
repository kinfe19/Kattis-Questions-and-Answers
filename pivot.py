
t = int(input())
l = [int(i) for i in input().split()]
mx = l[0]
p1 = [1]
for _ in range(1, t):
	if l[_] > mx:
		mx = l[_]
		p1.append(1)
	else:
		p1.append(0)
mn = l[-1]
p2 = [1]
for _ in range(2, t+1):
	if l[-_] < mn:
		mn = l[-_]
		p2.append(1)
	else:
		p2.append(0)
print(sum([p1[i] and p2[-i-1] for i in range(t)]))
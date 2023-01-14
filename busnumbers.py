n = int(input())
l = sorted([int(i) for i in input().split()])
p = []
x = []
f = 0
for i in range(n):
	if x != [] and l[i] == x[-1]+1:
		x.append(l[i])
		f += 1
	else:
		if f != 0:
			if f < 3:
				for j in range(f):
					print(x[j], end=' ')
			else:
				print(str(x[0])+'-'+str(x[-1]), end=' ')
		x = [l[i]]
		f = 1 
if f < 3:
	for j in range(f):
		print(x[j], end=' ')
else:
	print(str(x[0])+'-'+str(x[-1]), end=' ')
print()
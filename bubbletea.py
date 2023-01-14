n = int(input())
l = [int(i) for i in input().split()]
m = int(input())
p = [int(i) for i in input().split()]
z = []
for i in range(n):
	for j in [int(_) for _ in input().split()][1:]:
		z.append(p[j-1] + l[i])
print(max(int(input())//sorted(z)[0]-1, 0))
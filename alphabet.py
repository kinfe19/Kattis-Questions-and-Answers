s = input()
n = len(s)
l = [1 for i in range(n)]
for i in range(1, n):
	for j in range(0, i):
		if s[j] < s[i]:
			l[i] = max(l[i], l[j]+1)

print(26-max(l))
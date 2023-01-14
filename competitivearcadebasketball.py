n, k, m = map(int, input().split())
d = {}
for _ in range(n):
	d[input()] = 0
l = []
for _ in range(m):
	a, b = input().split()
	d[a] += int(b)
l = [i+' wins!' for i in d if d[i]>=k] 
if l == []:
	print('No winner!')
else:
	for _ in l:
		print(_)
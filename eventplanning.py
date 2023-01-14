n, c, h, m = map(int, input().split())
mn = float("Inf")
for i in range(h):
	d = int(input())
	if max([int(_) for _ in input().split()]) >= n and n*d <= c:
		mn = min(mn, n*d)
if mn == float("Inf"):
	print('stay home')
else:
	print(mn)
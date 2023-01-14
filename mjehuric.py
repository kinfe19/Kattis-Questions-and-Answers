
l = [int(i) for i in input().split()]
i = 0
while 1:
	if l == [1, 2, 3, 4, 5]:
		break
	if l[i+1] < l[i]:
		l[i], l[i+1] = l[i+1], l[i]
		print(*l)
	i += 1
	if i == 4:
		i = 0 
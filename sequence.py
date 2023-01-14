from math import log, ceil
k = log(int(input()), 2)
if k == int(k):
	k = int(k)+1
else:
	k = ceil(k)
print(k)
for i in range(k):
	print(2**i, end=' ')
print()
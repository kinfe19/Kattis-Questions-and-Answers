from itertools import combinations as com 

def pos(s):
	g = s[0]
	s = s[1:]
	d = []
	for j in range(0, 7):
		for i in com(list(s), j):
			d.append(''.join(sorted(list(i)+[g])))
	return d
d = pos(input())
for i in range(int(input())):
	s = input()
	if len(s)>3 and  ''.join(sorted(set(s))) in d:
		print(s)
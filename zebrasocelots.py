
s = ''
for i in range(int(input())):
	s += ['0', '1'][input()=='O']
print(int(s, 2)) 
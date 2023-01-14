p = 1
s = 1
for i in range(1, int(input())+1):
	p *= i 
	s += 1 / p 
print('%.20f'%s)

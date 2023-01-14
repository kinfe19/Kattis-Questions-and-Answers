s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a=input();b=input()
for i in range(len(a)):
	x = s.index(b[i])
	y = (s.index(a[i])+x)%26 
	if i % 2==0:
		y = (s.index(a[i])-x)%26 
	print(s[y], end='')
print()		

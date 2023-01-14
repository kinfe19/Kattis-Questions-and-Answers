a, b = map(int, input().split())
x = a*60 + b -45
if x < 0:
	x+=1440
a = x // 60 
b = x-a*60 
print(a, b)
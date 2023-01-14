for _ in range(int(input())):
	a, b = map(int, input().split())
	x = a+b 
	print((x**2+x+2) // 2+b)
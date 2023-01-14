n = int(input())
l = sorted([int(input()) for _ in range(n)], reverse=True)
s = sum(l) 
for i in range(n//3):
	s-=l[i*3+2]
print(s)
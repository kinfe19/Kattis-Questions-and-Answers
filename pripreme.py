input()
k = [int(i) for i in input().split()]
s = sum(k)
x = max(k)
k.remove(x) 
k = [0] + k 
c = sum(k)
if c < x:
	s += x-c 
print(s)
n = int(input())
c = 0 
while n % 2 == 0:
	n //= 2 
	c += 1 
for i in range(3, int(n**.5)+1, 2):
	while n % i == 0:
		n //= i 
		c += 1 
if n != 1:
	c += 1 
print(c)
from math import ceil
n =int(input())
l = []
for i in range(2, ceil(n/2)+1):
    if n%(2*i-1)==0 or (n-i)% (2*i-1)==0:
        l.append([i, i-1])
    if n % i == 0:
        l.append([i,i])
print(str(n)+':')
for i,j in l:
    print(str(i)+','+str(j))

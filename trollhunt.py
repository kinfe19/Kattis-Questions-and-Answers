from math import ceil
x,y,z = [int(i) for i in input().split()]
g = y//z
f = ceil((x-1)/g)
print(f)
l = [int(i)for i in input().split()]
a, b, c = l
x = 0
while c-b != 1:
    a, b = b, b+1
    x += 1

a, b, c = l
y = 0
while b-a != 1:
    b, c = b-1, b
    y += 1
print(max(x, y))
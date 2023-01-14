l = [[float(i) for i in input().split()]for _ in range(int(input()))]
s = 0
for i in range(len(l)-1):
    a, b = l[i]
    c, d = l[i+1]
    s += (b+d) / 2 * (c-a)
print(s / 1000)
x, y = [float(i) for i in input().split()]

p = 0;n = 0
for i in range(int(input())):
    j, k, l = [float(m) for m in input().split()]
    p += k - j
    n += (k-j) * l


print(x / ((y-p)+n))
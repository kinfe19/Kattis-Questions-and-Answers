n, m = map(int, input().split())
l = sum([int(input()) for i in range(m)])/n
print((-3*(n-m)/n)+l,  (3*(n-m)/n)+l)
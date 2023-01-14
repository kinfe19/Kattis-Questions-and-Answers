n = int(input())
c = 0
for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    c += a * b
print(c//n)
a, b = [int(i) for i in input().split()]
c = a+b
i = c
while 1:
    if c % i == 0 and (i-2)*(c//i-2)==b:
        print(i, c//i)
        break
    i -= 1
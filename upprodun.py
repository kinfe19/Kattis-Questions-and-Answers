a, b = [int(input()) for i in range(2)]
k = [b//a] * a
for i in range(b%a):
    k[i]+=1
for i in k:
    print('*' * i)
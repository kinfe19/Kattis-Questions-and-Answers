A = 'ABC'
B = 'BABC'
G = 'CCAABB'
n = int(input())
l = input()
d = {'Adrian':0, 'Bruno':0, 'Goran':0}
for i in range(n):
    j = l[i]
    if A[i%3] == j:
        d['Adrian'] += 1
    if B[i%4] == j:
        d['Bruno'] += 1
    if G[i%6] == j:
        d['Goran'] += 1
h = max(d.values())
print(h)
for i in d:
    if d[i] == h:
        print(i)

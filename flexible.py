from itertools import combinations as cm
n, m =[int(i) for i in input().split()]
l = [int(i) for i in input().split()]
l.extend([0, n])

print(*sorted(set([abs(i-j)for i, j in cm(l, 2)])))
from math import log
l = ['Your wish is granted!', 'You will become a flying monkey!']
a, b = map(int, input().split())
print(l[b < log(a, 2)])
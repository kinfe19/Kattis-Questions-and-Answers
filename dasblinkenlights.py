from math import gcd 
p, q, s = [int(i) for i in input().split()]
k = p*q // gcd(p,q)
if k<=s:print('yes')
else:print('no')
l=[]
for i in range(int(input())):
    l.append(input())
if sorted(l)==l:
    print('INCREASING')
elif sorted(l)==l[::-1]:
    print('DECREASING')
else:
    print('NEITHER')

def binsearch(l, key):
    low=0
    high=len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] == key:
            return 'found'
        elif l[mid] > key:
            high = mid-1
        else:
            low = mid + 1
    return 'not found'

n,m,a,c,x0 = [int(i) for i in input().split()]
xs = []
xs.append(x0)
for i in range(n):
    b = ((a%m*xs[-1]%m)%m+c%m)%m
    xs.append( b )
xs = xs[1:]
num = 0
for i in xs:
    if binsearch(xs, i) == 'found':
        num += 1

print( num )
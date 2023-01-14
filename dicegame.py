e = sum([int(i) for i in input().split()])
g = sum([int(i) for i in input().split()])
if e<g:
    print('Emma')
elif g<e:
    print('Gunnar')
else:
    print('Tie')
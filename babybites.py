n =int(input())
g = 1
l = input().split()
for i in range(n):
    if l[i] != 'mumble' and l[i] != str(i+1):
        g=0
if g:
    print('makes sense')
else:
    print('something is fishy')

x,y,z = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
block = True

while block and x:
    sm = 0
    while 1:
        sm += a[0]
        a = a[1:]
        if sm == y:
            break
        if sm > y:
            block = False
            break
    
    x -= 1
           

if block:
    print("YES")
else:
    print("NO")
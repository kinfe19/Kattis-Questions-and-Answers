t = int(input())
for i in range(t):
    n = int(input())
    l = [int(input()) for j in range(n)]
    s = max(l)
    if l.count(s) > 1:
        print('no winner')
    else:
        v =l.index(s)+1
        if s > sum(l)/2:
            print(f'majority winner {v}')
        else:
            print(f'minority winner {v}')
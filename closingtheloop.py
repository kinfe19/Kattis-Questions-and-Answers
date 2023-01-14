t = int(input())
for _ in range(1, t+1):
    input()
    r = []
    b = []
    for i in input().split():
        if i[-1] == 'R':
            r.append(int(i[:-1]))
        else:
            b.append(int(i[:-1]))
    if r == [] or b == []:
        print(f'Case #{_}:', 0)
    else:
        r.sort(reverse=True)
        b.sort(reverse=True)
        a = min(len(r), len(b))
        print(f'Case #{_}:', sum(r[:a])+sum(b[:a])-a-a)

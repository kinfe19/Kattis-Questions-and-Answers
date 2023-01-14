def ch(n):
    if n%2:
        return 3*n +1
    else:
        return n//2

def form(v, a, la, b, lb):
    return f'{a} needs {la.index(v)} steps, {b} needs {lb.index(v)} steps, they meet at {v}'
a, b = [int(i) for i in input().split()]

while a+b != 0:
    la = [a]
    lb = [b]
    while (la[-1] not in lb) and (lb[-1] not in la):
        if la[-1] != 1:
            la.append(ch(la[-1]))
        if lb[-1] != 1:
            lb.append(ch(lb[-1]))
    v = la[-1] if la[-1] in lb else lb[-1]
    print(form(v, a, la, b, lb))
    a, b = [int(i) for i in input().split()]
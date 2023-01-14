a = input().split()
l = [input().split() for i in range(int(input()))]
for _ in range(int(input())):
    k = a.index(input())
    l.sort(key=lambda x:x[k])
    print(*a)
    for i in l:
        print(*i)
    print()
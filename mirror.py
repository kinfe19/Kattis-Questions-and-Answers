for i in range(int(input())):
    a,b = [int(j)for j in input().split()]
    l = []
    for j in range(a):
        l.append(input()[::-1])
    l.reverse()
    print('Test',i+1)
    for j in l:
        print(j)
                
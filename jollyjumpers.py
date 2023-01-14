while True:
    try:
        l = [int(i) for i in input().split()][1:]
        g = [abs(l[i]-l[i-1])for i in range(1,len(l))]
        print('Jolly' if sorted(g)==list(range(1, len(l))) else 'Not jolly')
    except:
        break
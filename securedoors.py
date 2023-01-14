d={}
n=int(input())
for i in range(n):
    a,b=input().split()
    if a=='entry':
        if b in d:
            print(b,'entered (ANOMALY)')
        else:
            d[b]=1
            print(b,'entered')
    else:
        if b not in d:
            print(b,'exited (ANOMALY)')
        else:
            del(d[b])
            print(b,'exited')

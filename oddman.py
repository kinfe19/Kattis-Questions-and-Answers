n=int(input())
for i in range(n):
    c=int(input())
    j=input().split()
    for s in j:
        if(j.count(s)==1):
            print('Case #'+str(i+1)+": "+s)
            

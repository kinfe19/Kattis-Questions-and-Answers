n=int(input())
l=[]
for i in range(n):
    h=input().split()
    if(len(h)>=2):
        if(h[0]=="Simon" and h[1]=="says"):
            print(*h[2:],sep=" ")

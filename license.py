v=int(input())
j=input().split()
g=[]
for i in j:
    g.append(int(i))
print(g.index(min(g)))

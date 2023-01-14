n=int(input());t=(n//3)*3;s=0
l=sorted([int(i) for i in input().split()], reverse=True)[:t]
for i in range(2, t, 3):s+=l[i]
print(s)
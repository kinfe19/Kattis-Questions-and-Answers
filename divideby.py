a=input()[::-1]
b=len(input())-1
c=0
if b>=len(a):
    c=b-len(a)+1
a+='0'*c
l=a[:b]+'.'+a[b:]
k=''
i=0
for j in l:
    if j=='.':
        k+=l[i+1:]
        break
    if j!='0':
        k+=l[i:]
        break
    i+=1
print(k[::-1])
    

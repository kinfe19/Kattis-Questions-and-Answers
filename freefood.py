n=int(input())
st=[]
for i in range(n):
    g=input().split()
    a=int(g[0])
    b=int(g[1])
    for j in range(a,b+1):
        if not(j in st):
            st.append(j)

print(len(st))
    

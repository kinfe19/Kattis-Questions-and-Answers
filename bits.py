for i in range(int(input())):
    k=input()
    c=0
    ss=''
    for i in range(len(k)):
        ss+=k[i]
        l=bin(int(ss)).count('1')
        if l>c:
            c=l
    print(c)
    

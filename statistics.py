j=1
while True:
    try:
        l=[int(i)for i in input().split()]
        l=l[1:]
        print('Case '+str(j)+':',min(l),max(l),max(l)-min(l))
        j+=1
    except:
        break

a,b=[int(i)for i in input().split()]
if b>a:
    if b-a==1:
        print("Dr. Chaz will have 1 piece of chicken left over!")
    else:
        print("Dr. Chaz will have",b-a,"pieces of chicken left over!")
else:
    if a-b==1:
        print("Dr. Chaz needs 1 more piece of chicken!")
    else:
        print("Dr. Chaz needs",a-b," more pieces of chicken!")
    

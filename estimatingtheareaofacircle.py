from math import pi
l=[float(i)for i in input().split()]
while l!=[0,0,0]:
    print('%.5f'%(pi*l[0]**2),'%.5f'%((2*l[0])**2*l[2]/l[1]))
    l=[float(i)for i in input().split()]

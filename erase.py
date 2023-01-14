n = int(input())
a = input()
b = input()
c = ''.join([str(int(not int(i))) for i in b])
if (n % 2==1 and a==c) or (n%2==0 and a==b):
    print('Deletion succeeded')
else:
    print('Deletion failed')
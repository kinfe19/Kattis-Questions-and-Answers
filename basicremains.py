def tobase10(n, b):
    if b==10:return int(n)
    s=0
    for i in range(len(n)):
        s+=int(n[-i-1])*pow(b, i)
    return s
def tobaseb(n, b):
    r=''
    while n!=0:
        n, a = n//b, n%b
        r+=str(a)
    return r[::-1] if r!='' else '0'

l = input().split()
while len(l) != 1:
    b, p, m = l
    b = int(b)
    print(tobaseb(pow(int(p, b), 1, int(m, b)), b))
    l = input().split()
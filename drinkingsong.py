n=int(input())
s=input()
for i in range(n):
    if n-i==1:
        print("1 bottle of",s,'on the wall, 1 bottle of',s+'.')
    else:
        print(n-i,'bottles of',s,'on the wall,', n-i ,'bottles of',s+'.')
    if n-i==2:
        print('Take one down, pass it around, 1 bottle of',s,'on the wall.')
    elif n-i==1:
        print('Take it down, pass it around, no more bottles of',s+'.')
    else:
        print('Take one down, pass it around,', n-i-1 ,'bottles of',s,'on the wall.')
    print()
##    if i!=n-1:
##        print()
##3 bottles of milk on the wall, 3 bottles of milk.
##Take one down, pass it around, 2 bottles of milk on the wall.
##
##2 bottles of milk on the wall, 2 bottles of milk.
##Take one down, pass it around, 1 bottle of milk on the wall.
##
##1 bottle of milk on the wall, 1 bottle of milk.
##Take it down, pass it around, no more bottles of milk.

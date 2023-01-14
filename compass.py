a, b = [int(input())for i in range(2)]
if b < a:
    b+=360
c = b-a

print(c if c<=180 else c-360)
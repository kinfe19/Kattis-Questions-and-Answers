f, g, h = [int(i) for i in input().split()]
b = f*3 + g*2 + h
s = []
if b >= 8:
    s.append("Province")
elif b >= 5:
    s.append("Duchy")
elif(b>=2):
    s.append("Estate")
if s != []:
    s.append("or")
if b >= 6:
    s.append("Gold")
elif b >= 3:
    s.append("Silver")
else:
    s.append("Copper")

print(" ".join(s))
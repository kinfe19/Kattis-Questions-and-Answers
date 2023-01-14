s = input()
a = s[-1]
x = int(input())
l = []
start = []
end = []
for i in range(26):
    start.append(0)
for i in range(x):
    y = input()
    if y[0] == a:
        l.append(y)
    start[ord(y[0]) - ord('a')] += 1
if l == []:
    print("?")
else:
    f = 0
    for i in l:
        if i[0] != i[-1]:
            if start[ord(i[-1]) - ord('a')] == 0:
                print(i + "!")
                f = 1
                break
        else:
            if start[ord(i[-1]) - ord('a')] == 1:
                print(i + "!")
                f = 1
                break
    if f == 0:
        print(l[0])

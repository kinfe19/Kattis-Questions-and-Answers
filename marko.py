r = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
d = {}
for i in range(len(r)):
    for j in r[i]:
        d[j] = str(i+1)
t = [''.join(d[i] for i in input()) for _ in range(int(input()))]
s = input()
try:
    print(t.count(s))
except:
    print(0)
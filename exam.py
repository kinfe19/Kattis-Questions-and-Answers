correct = int(input())
n = input()
s = input()
questions=len(s)
same = 0
for i in range( questions ):
    if s[i] == n[i]:
        same += 1
miss = questions - correct
diff = questions - same
score = 0
if diff < miss:
    score += diff
else:
    score += miss
if same > correct:
    score += correct
else:
    score += same
print(score)
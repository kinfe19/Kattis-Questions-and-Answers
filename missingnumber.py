n = int(input())
s = input()
for i in range(1, n+1):
	k = str(i)
	if s[:len(k)] == str(i):
		s = s[len(k):]
	else:
		print(i)
		break

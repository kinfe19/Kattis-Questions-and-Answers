n = int(input())
l = [int(_) for _ in input().split()]
st = []
for i in l:
	if st != []:
		if (st[-1] + i) % 2 == 0:
			st.pop()
		else:
			st.append(i)
	else:
		st.append(i)
print(len(st))
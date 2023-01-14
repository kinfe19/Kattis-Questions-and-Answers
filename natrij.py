a, b = [[int(i) for i in input().split(':')] for _ in range(2)]
sec = 0
while a != b:
	if a[2] == 59:
		a[2] = 0 
		if a[1] == 59:
			a[1] = 0
			if a[0] == 23:
				a[0] = 0 
			else:
				a[0] += 1 
		else:
			a[1] += 1
	else:
		a[2] += 1
	sec += 1 
if sec == 0:
    print('24:00:00')
else:
    h = str(sec // 3600)
    sec -= int(h) * 3600 
    m = str(sec // 60)
    s = str(sec % 60)
    
    print('0'*(2-len(h))+h+':'+'0'*(2-len(m))+m+':'+'0'*(2-len(s))+s)
var = {}
while 1:
	s = input()
	if s == '0':
		break 
	if '=' in s:
		l = s.split(' = ')
		var[l[0]] = int(l[1])
	else:
		l = s.split(' + ')
		nn = []
		vr = []
		for i in l:
			if i.isdigit():
				nn.append(int(i))
			elif i in var:
				nn.append(var[i])
			else:
				vr.append(i)
		if nn != []:
			vr = [str(sum(nn))] + vr 
		print(' + '.join(vr)) 
  
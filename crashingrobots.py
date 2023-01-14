dr = ['N', 'E', 'S', 'W']
dl = ['N', 'W', 'S', 'E']
def dir(curr, dirc, times):
	if dirc == 'L':
		return dl[(dl.index(curr)+ times)%4]
	elif dirc == 'R':
		return dr[(dr.index(curr)+ times)%4]

def crash(a, b, c, d, t, f):
	# print((a, b, c, d, t, f))
	if a == c:
		if f:
			for _ in range(b, b+t+1):
				if d == _:
					return True, 99999999-_
		else:
			for _ in range(b-t, b+1):
				if d == _:
					return True, _
	return False, -99999999
def printify(rob_data, w, h):
	p = [[0 for _ in range(h)] for __ in range(w)]
	for i, j, k, l in rob_data:
		#print(f'robot {i} at ({j}, {k}) in {l}')
		p[k][j] = i 
	p = map(list, zip(*p))
	for i in p:
		print(*i)
	print()

def che(curr_id, rob_data, width, length, times):
	# 0 - nothing 1 - wall 2 - robot
	_, x, y, dirc = rob_data[curr_id-1]
	robot = False
	wall = False
	crash_id = None
	if dirc == 'E':
		vv = []
		for ids, xx, yy, _ in rob_data:
			if ids != curr_id and crash(x, y, xx, yy, times, 1)[0]:
				robot = True
				vv.append([crash(x, y, xx, yy, times, 1)[1], ids])
				# print('-------------crash1')
		if robot:
			crash_id = sorted(vv)[-1][1]	
		if not robot and y+times >= width:
			# print('++++++++++++++wall-1')
			wall = True
		else:
			y += times
	elif dirc == 'W':
		vv = []
		for ids, xx, yy, _ in rob_data:
			if ids != curr_id and crash(x, y, xx, yy, times, 0)[0]:
				robot = True
				vv.append([crash(x, y, xx, yy, times, 0)[1], ids])
				# print('-------------crash2')
		if robot:
			crash_id = sorted(vv)[-1][1]
		if not robot and y-times < 0:
			# print('++++++++++++++wall-2')
			wall = True
		else:
			y -= times
	elif dirc == 'S':
		vv = []
		for ids, xx, yy, _ in rob_data:
			if ids != curr_id and crash(y, x, yy, xx, times, 1)[0]:
				robot = True
				vv.append([crash(y, x, yy, xx, times, 1)[1], ids])
				# print('-------------crash3')
		if robot:
			crash_id = sorted(vv)[-1][1]
		if not robot and x+times >= length:
			# print('++++++++++++++wall-3')
			wall = True
		else:
			x += times
	elif dirc == 'N':
		vv = []
		for ids, xx, yy, _ in rob_data:
			if ids != curr_id and crash(y, x, yy, xx, times, 0)[0]:
				robot = True
				vv.append([crash(y, x, yy, xx, times, 0)[1], ids])
				# print('-------------crash4')		
		if robot:
			crash_id = sorted(vv)[-1][1]
		if not robot and x-times < 0:
			# print('++++++++++++++wall-4', y, times)
			wall = True
		else:
			x -= times
	return x, y, robot, wall, crash_id

for __ in range(int(input())):
	R, C = map(int, input().split())
	rob, com = map(int, input().split())
	rob_id_pos_dir = []
	for _ in range(1, rob+1):
		x, y, d = input().split()
		rob_id_pos_dir.append([_, C-int(y), int(x)-1, d])
	first = None
	# printify(rob_id_pos_dir, R, C)
	for _ in range(com):
		i, j, k = input().split()
		idd, tim = map(int, [i, k])
		if j == 'F':
			x, y, rb, wl, crash_id = che(idd, rob_id_pos_dir, R, C, tim)
			if rb and first == None:
				first = f'Robot {idd} crashes into robot {crash_id}'
			elif wl and first == None:
				first = f'Robot {idd} crashes into the wall'
			else:
				bac = rob_id_pos_dir[idd-1]
				rob_id_pos_dir[idd-1] = [idd, x, y, bac[-1]]
		else:
			bac = rob_id_pos_dir[idd-1]
			new_dir = dir(bac[-1], j, tim)
			rob_id_pos_dir[idd-1] = [idd, bac[1], bac[2], new_dir]
		# printify(rob_id_pos_dir, R, C)
	print('OK' if not first else first)

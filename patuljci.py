ls = [int(input()) for i in range(9)]

flag = False
for i in range(8):
    x = ls[i]
    ls[i] = 0
    for j in range(i+1, 9):
        y = ls[j]
        ls[j] = 0
        if sum(ls) == 100:
            flag = True
            break

        ls[j] = y
        
    if flag:
        break
    ls[i] = x

print('\n'.join([str(i) for i in ls if i != 0]))

